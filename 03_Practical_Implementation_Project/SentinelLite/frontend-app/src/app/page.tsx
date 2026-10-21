
"use client";

import { useState } from "react";

import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
  Legend,
} from "recharts";


type Summary = {
  total_rows: number;
  valid_rows: number;
  invalid_rows: number;
  alerts_detected: number;
};

type ApiAlert = Record<string, unknown>;

type ApiResult = {
  filename: string;
  summary: Summary;
  invalid_rows: unknown[];
  alerts: ApiAlert[];
};

const API_URL = "http://127.0.0.1:8000/api/analyze";
const MAX_FILE_SIZE = 5 * 1024 * 1024;

function field(
  item: ApiAlert,
  keys: string[],
  fallback = "—",
): string {
  for (const key of keys) {
    const value = item[key];
    if (value !== undefined && value !== null && String(value).trim()) {
      return String(value);
    }
  }
  return fallback;
}

function severityClass(severity: string) {
  const value = severity.toLowerCase();
  if (value === "high" || value === "critical") {
    return "border-rose-400/30 bg-rose-400/10 text-rose-300";
  }
  if (value === "low") {
    return "border-cyan-400/30 bg-cyan-400/10 text-cyan-300";
  }
  return "border-amber-400/30 bg-amber-400/10 text-amber-300";
}

const rules = [
  { id: "DET-01", title: "Brute-Force Detection", severity: "Medium", description: "Repeated failed login attempts" },
  { id: "DET-02", title: "Suspicious Successful Login", severity: "High", description: "Successful login after repeated failures" },
  { id: "DET-03", title: "Unapproved Privilege Change", severity: "Medium", description: "Privilege change outside the allowlist" },
];

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<ApiResult | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [severityFilter, setSeverityFilter] = useState("All");
  const [searchTerm, setSearchTerm] = useState("");

  function selectFile(selected: File | null) {
    setError("");
    setResult(null);

    if (!selected) {
      setFile(null);
      return;
    }
    if (!selected.name.toLowerCase().endsWith(".csv")) {
      setFile(null);
      setError("Please select a CSV file.");
      return;
    }
    if (selected.size > MAX_FILE_SIZE) {
      setFile(null);
      setError("File exceeds the 5 MB upload limit.");
      return;
    }
    setFile(selected);
  }

  async function analyzeLogs() {
    if (!file || loading) return;

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const body = new FormData();
      body.append("file", file);

      const response = await fetch(API_URL, {
        method: "POST",
        body,
      });

      const data = await response.json().catch(() => null);

      if (!response.ok) {
        throw new Error(
          typeof data?.detail === "string"
            ? data.detail
            : `Analysis failed with HTTP ${response.status}.`,
        );
      }

      if (!data?.summary || !Array.isArray(data.alerts)) {
        throw new Error("The API returned an unexpected response.");
      }

      setResult(data as ApiResult);
    } catch (err) {
      setError(
        err instanceof TypeError
          ? "Cannot connect to FastAPI. Make sure the backend is running at 127.0.0.1:8000."
          : err instanceof Error
            ? err.message
            : "An unexpected error occurred.",
      );
    } finally {
      setLoading(false);
    }
  }

  const alerts = result?.alerts ?? [];

  const severityData = ["High", "Medium", "Low"].map((severity) => ({
    name: severity,
    value: alerts.filter(
      (alert) =>
        field(alert, ["severity", "level", "risk"], "Medium").toLowerCase() ===
        severity.toLowerCase()
    ).length,
  }));
  
  const chartColors: Record<string, string> = {
    High: "#fb7185",
    Medium: "#fbbf24",
    Low: "#22d3ee",
  };
  const filteredAlerts = alerts.filter((alert) => {
    const severity = field(alert, ["severity", "level", "risk"], "Medium");
    const matchesSeverity =
      severityFilter === "All" ||
      severity.toLowerCase() === severityFilter.toLowerCase();
  
    const searchableText = [
      field(alert, ["title", "name", "description", "message"]),
      field(alert, ["actor", "username", "user"]),
      field(alert, ["rule_id", "rule", "rule_code", "detection_id"]),
      field(alert, ["timestamp", "time", "event_time", "detected_at"]),
    ]
      .join(" ")
      .toLowerCase();
  
    const matchesSearch = searchableText.includes(
      searchTerm.trim().toLowerCase()
    );
  
    return matchesSeverity && matchesSearch;
  });
  

  const metrics = [
    {
      label: "Total Log Events",
      value: result?.summary.total_rows ?? "—",
      note: "CSV records processed",
      icon: "≡",
      color: "text-cyan-300",
    },
    {
      label: "Alerts Detected",
      value: result?.summary.alerts_detected ?? "—",
      note: "Detection engine results",
      icon: "⚑",
      color: "text-amber-300",
    },
    {
      label: "Valid Rows",
      value: result?.summary.valid_rows ?? "—",
      note: "Validated records",
      icon: "✓",
      color: "text-emerald-300",
    },
    {
      label: "Invalid Rows",
      value: result?.summary.invalid_rows ?? "—",
      note: "Records needing review",
      icon: "!",
      color: "text-rose-300",
    },
  ];

  return (
    <main className="min-h-screen bg-[#080f1d] text-slate-100 md:flex">
      <aside className="border-b border-slate-800 bg-[#0c1627] p-5 md:min-h-screen md:w-64 md:border-b-0 md:border-r">
        <div className="flex items-center gap-3">
          <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-cyan-400/10 text-cyan-300">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" className="h-7 w-7">
              <path d="M12 3 20 6v5c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6l8-3Z" />
              <path d="m9 12 2 2 4-4" />
            </svg>
          </div>
          <div>
            <h1 className="text-lg font-bold tracking-wide">SentinelLite</h1>
            <p className="text-[10px] tracking-[0.15em] text-slate-500">SECURITY OPERATIONS</p>
          </div>
        </div>


        <p className="mb-3 mt-9 text-xs font-semibold uppercase tracking-[0.18em] text-slate-500">Workspace</p>
        <nav className="space-y-2">
          <a href="#overview" className="flex items-center gap-3 rounded-xl border border-cyan-400/20 bg-cyan-400/10 px-4 py-3 text-sm text-cyan-200">◈ <span>Overview</span></a>
          <a href="#upload" className="flex items-center gap-3 rounded-xl px-4 py-3 text-sm text-slate-400 transition hover:bg-slate-800 hover:text-white">↥ <span>Log Analysis</span></a>
          <a href="#alerts" className="flex items-center gap-3 rounded-xl px-4 py-3 text-sm text-slate-400 transition hover:bg-slate-800 hover:text-white">⚑ <span>Security Alerts</span></a>
          <a href="#rules" className="flex items-center gap-3 rounded-xl px-4 py-3 text-sm text-slate-400 transition hover:bg-slate-800 hover:text-white">≡ <span>Detection Rules</span></a>
        </nav>

        <div className="mt-10 rounded-xl border border-slate-800 bg-[#101d30] p-4">
          <div className="flex items-center gap-2 text-sm font-medium">
            <span className={`h-2 w-2 rounded-full ${error ? "bg-rose-400" : result ? "bg-emerald-400" : "bg-amber-400"}`} />
            Local API
          </div>
          <p className="mt-2 text-xs text-slate-500">Endpoint</p>
          <p className="break-all text-xs text-cyan-300">127.0.0.1:8000</p>
          <p className="mt-2 text-xs text-slate-500">{result ? "Analysis completed" : error ? "Check connection or input" : "Ready for analysis"}</p>
        </div>

        <div className="mt-4 rounded-xl border border-slate-800 p-4">
          <p className="text-xs font-semibold text-slate-300">Detection Engine</p>
          <p className="mt-2 text-xs leading-5 text-slate-500">Rule-based log analysis for suspicious login activity and privilege changes.</p>
        </div>
      </aside>

      <section className="min-w-0 flex-1">
        <header className="flex flex-wrap items-center justify-between gap-4 border-b border-slate-800 px-6 py-5 lg:px-9">
          <div>
            <p className="text-xs text-slate-500">SECURITY / OVERVIEW</p>
            <h2 className="mt-1 text-xl font-semibold">Command Center</h2>
          </div>
          <div className="flex items-center gap-2 rounded-full border border-slate-700 bg-slate-900/70 px-3 py-2 text-xs text-slate-300">
            <span className={`h-2 w-2 rounded-full ${result ? "bg-emerald-400" : "bg-amber-400"}`} />
            {result ? "Analysis complete" : "Local development"}
          </div>
        </header>

        <div className="space-y-8 p-5 sm:p-7 lg:p-9">

          <section id="overview">
            <div className="mb-5">
              <p className="text-sm text-slate-400">Welcome to SentinelLite</p>
              <h3 className="mt-1 text-2xl font-bold tracking-tight sm:text-3xl">Security Overview<span className="text-cyan-300">.</span></h3>
              <p className="mt-2 text-sm text-slate-500">Analyze security logs and identify suspicious activity.</p>
            </div>

            <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
              {metrics.map((metric) => (
                <article key={metric.label} className="rounded-2xl border border-slate-800 bg-[#0d1829] p-5 transition hover:border-slate-700">
                  <div className="flex items-center justify-between">
                    <p className="text-sm text-slate-400">{metric.label}</p>
                    <span className={`text-xl ${metric.color}`}>{metric.icon}</span>
                  </div>
                  <p className="mt-5 text-3xl font-semibold">{metric.value}</p>
                  <p className="mt-2 text-xs text-slate-500">{metric.note}</p>
                </article>
              ))}
            </div>
             <div className="mt-6 rounded-2xl border border-slate-800 bg-[#0d1829] p-5 sm:p-6">
              <div className="mb-4">
                <h3 className="font-semibold">Alert Analytics</h3>
                <p className="mt-1 text-sm text-slate-500">
                  Severity distribution for the analyzed log file
                </p>
              </div>

              {!result ? (
                <div className="flex min-h-56 items-center justify-center text-center text-sm text-slate-500">
                  Upload and analyze a CSV to view alert analytics.
                </div>
              ) : alerts.length === 0 ? (
                <div className="flex min-h-56 items-center justify-center text-sm text-emerald-300">
                  No alerts detected.
                </div>
              ) : (
                <div className="h-72 w-full">
                  <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                      <Pie
                        data={severityData}
                        dataKey="value"
                        nameKey="name"
                        cx="50%"
                        cy="50%"
                        innerRadius={65}
                        outerRadius={100}
                        paddingAngle={4}
                      >
                        {severityData.map((entry) => (
                          <Cell key={entry.name} fill={chartColors[entry.name]} />
                        ))}
                      </Pie>
                      <Tooltip
                        contentStyle={{
                          backgroundColor: "#0c1627",
                          border: "1px solid #334155",
                          borderRadius: "12px",
                          color: "#f1f5f9",
                        }}
                      />
                      <Legend />
                    </PieChart>
                  </ResponsiveContainer>
                </div>
              )}
            </div>
          </section>

          <section id="upload" className="rounded-2xl border border-slate-800 bg-[#0d1829] p-5 sm:p-7">
            <div className="flex flex-wrap items-start justify-between gap-3">
              <div>
                <h3 className="text-lg font-semibold">Analyze Security Logs</h3>
                <p className="mt-1 text-sm text-slate-400">Upload a CSV file to run server-side validation and detection.</p>
              </div>
              <span className="rounded-lg border border-slate-700 px-3 py-1.5 text-xs text-slate-400">MAX 5 MB</span>
            </div>

            <label className="mt-6 flex cursor-pointer flex-col items-center rounded-xl border border-dashed border-slate-700 bg-[#091321] px-5 py-9 text-center transition hover:border-cyan-400/60 hover:bg-cyan-400/[0.03]">
              <span className="flex h-12 w-12 items-center justify-center rounded-xl bg-cyan-400/10 text-2xl text-cyan-300">↥</span>
              <span className="mt-4 break-all text-sm font-medium">{file ? file.name : "Choose a CSV file"}</span>
              <span className="mt-2 text-xs text-slate-500">{file ? `${(file.size / 1024).toFixed(1)} KB selected` : "CSV format · Maximum file size 5 MB"}</span>
              <input type="file" accept=".csv,text/csv" className="sr-only" disabled={loading} onChange={(event) => selectFile(event.target.files?.[0] ?? null)} />
            </label>

            {error && <div role="alert" className="mt-4 rounded-xl border border-rose-400/20 bg-rose-400/10 px-4 py-3 text-sm text-rose-200">{error}</div>}
            {result && <div role="status" className="mt-4 rounded-xl border border-emerald-400/20 bg-emerald-400/10 px-4 py-3 text-sm text-emerald-200">Analysis completed successfully for {result.filename}.</div>}

            <button type="button" onClick={analyzeLogs} disabled={!file || loading} className="mt-4 w-full rounded-xl bg-cyan-300 px-5 py-3 text-sm font-semibold text-slate-950 transition hover:bg-cyan-200 disabled:cursor-not-allowed disabled:bg-slate-700 disabled:text-slate-400 sm:w-auto">
              {loading ? "Analyzing logs…" : "Analyze Logs →"}
            </button>
            <p className="mt-3 text-xs text-slate-500">Files are sent to your local SentinelLite API for analysis.</p>
          </section>

          <section id="alerts" className="overflow-hidden rounded-2xl border border-slate-800 bg-[#0d1829]">
            <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 px-5 py-5 sm:px-6">
              <div>
                <h3 className="font-semibold">Security Alerts</h3>
                <p className="mt-1 text-xs text-slate-500">{result ? "Detection engine results for the uploaded CSV" : "Upload and analyze a CSV to view real alerts"}</p>
              </div>
              <span className="rounded-lg border border-slate-700 px-3 py-1.5 text-xs text-slate-400">{result ? `${alerts.length} alerts` : "No results"}</span>
            </div>

            <div className="space-y-4 border-b border-slate-800 p-5 sm:px-6">
  <input
    type="search"
    value={searchTerm}
    onChange={(event) => setSearchTerm(event.target.value)}
    placeholder="Search alert, actor, rule ID..."
    aria-label="Search security alerts"
    className="w-full rounded-xl border border-slate-700 bg-[#091321] px-4 py-3 text-sm text-slate-100 outline-none placeholder:text-slate-500 focus:border-cyan-400 sm:max-w-md"
  />

  <div className="flex flex-wrap items-center gap-2">
    <span className="mr-1 text-xs text-slate-500">Severity:</span>

    {["All", "High", "Medium", "Low"].map((severity) => (
      <button
        key={severity}
        type="button"
        onClick={() => setSeverityFilter(severity)}
        aria-pressed={severityFilter === severity}
        className={`rounded-lg border px-3 py-2 text-xs font-medium transition ${
          severityFilter === severity
            ? "border-cyan-400/40 bg-cyan-400/10 text-cyan-200"
            : "border-slate-700 text-slate-400 hover:border-slate-500 hover:text-white"
        }`}
      >
        {severity}
      </button>
    ))}
  </div>

  <p className="text-xs text-slate-500">
    Showing {filteredAlerts.length} of {alerts.length} alerts
  </p>
</div>

            <div className="overflow-x-auto">
              <table className="w-full min-w-[700px] text-left text-sm">
                <thead className="bg-[#101d30] text-xs uppercase tracking-wider text-slate-500">
                  <tr>
                    <th className="px-5 py-4 font-medium">Alert</th>
                    <th className="px-5 py-4 font-medium">Actor</th>
                    <th className="px-5 py-4 font-medium">Rule</th>
                    <th className="px-5 py-4 font-medium">Timestamp</th>
                    <th className="px-5 py-4 font-medium">Severity</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/80">
                {filteredAlerts.map((alert, index) => {
                    const title = field(alert, ["title", "name", "description", "message"], "Suspicious activity detected");
                    const severity = field(alert, ["severity", "level", "risk"], "Medium");
                    return (
                      <tr key={`${field(alert, ["rule_id", "rule", "rule_code"], "alert")}-${index}`} className="transition hover:bg-slate-800/30">
                        <td className="px-5 py-4">
                          <p className="font-medium text-slate-200">{title}</p>
                          <p className="mt-1 text-xs text-slate-500">{field(alert, ["id", "alert_id"], `ALT-${String(index + 1).padStart(3, "0")}`)}</p>
                        </td>
                        <td className="px-5 py-4 font-mono text-slate-300">{field(alert, ["actor", "username", "user"])}</td>
                        <td className="px-5 py-4"><span className="rounded-md border border-slate-700 px-2 py-1 text-xs text-slate-300">{field(alert, ["rule_id", "rule", "rule_code", "detection_id"])}</span></td>
                        <td className="px-5 py-4 text-slate-400">{field(alert, ["timestamp", "time", "event_time", "detected_at"])}</td>
                        <td className="px-5 py-4"><span className={`rounded-full border px-2.5 py-1 text-xs font-medium ${severityClass(severity)}`}>{severity}</span></td>
                      </tr>
                    );
                  })}
                  {result && filteredAlerts.length === 0 && (
  <tr>
    <td colSpan={5} className="px-5 py-10 text-center text-sm text-slate-500">
      {alerts.length === 0
        ? "No security alerts detected in this CSV."
        : "No alerts match your search or severity filter."}
    </td>
  </tr>
)}
                </tbody>
              </table>
            </div>
          </section>

          {result && result.invalid_rows.length > 0 && (
            <section className="rounded-2xl border border-rose-400/20 bg-[#0d1829] p-5 sm:p-6">
              <h3 className="font-semibold text-rose-200">Invalid Rows</h3>
              <p className="mt-1 text-sm text-slate-400">{result.invalid_rows.length} record(s) need review.</p>
              <pre className="mt-4 max-h-64 overflow-auto whitespace-pre-wrap break-words rounded-xl bg-[#091321] p-4 text-xs text-slate-300">{JSON.stringify(result.invalid_rows, null, 2)}</pre>
            </section>
          )}

          <section id="rules" className="rounded-2xl border border-slate-800 bg-[#0d1829] p-5 sm:p-6">
            <h3 className="font-semibold">Detection Rules</h3>
            <p className="mt-1 text-sm text-slate-500">Current rule-based detection capabilities</p>
            <div className="mt-5 grid gap-3 md:grid-cols-3">
              {rules.map((rule) => (
                <article key={rule.id} className="rounded-xl border border-slate-800 bg-[#091321] p-4">
                  <div className="flex items-center justify-between gap-2">
                    <p className="font-mono text-xs text-cyan-300">{rule.id}</p>
                    <span className={`rounded-full border px-2 py-1 text-[10px] ${severityClass(rule.severity)}`}>{rule.severity}</span>
                  </div>
                  <p className="mt-3 text-sm font-medium">{rule.title}</p>
                  <p className="mt-2 text-xs leading-5 text-slate-500">{rule.description}</p>
                </article>
              ))}
            </div>
          </section>

          <footer className="border-t border-slate-800 pt-5 text-xs text-slate-600">SentinelLite · Rule-based security log analysis · Local development</footer>
        </div>
      </section>
    </main>
  );
}
