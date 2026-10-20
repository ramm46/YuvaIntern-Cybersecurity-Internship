"use client";

import { useState } from "react";

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

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<ApiResult | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function analyzeLogs() {
    if (!file || loading) return;

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(API_URL, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          typeof data.detail === "string"
            ? data.detail
            : `Request failed: ${response.status}`,
        );
      }

      setResult(data as ApiResult);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Unable to analyze the file.",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-[#080f1d] p-5 text-slate-100 sm:p-10">
      <header className="mb-8 border-b border-slate-800 pb-5">
        <h1 className="text-3xl font-bold text-cyan-300">
          SentinelLite
        </h1>
        <p className="mt-2 text-sm text-slate-400">
          Security Operations · Log Analysis
        </p>
      </header>

      <section className="max-w-3xl rounded-2xl border border-slate-800 bg-[#0d1829] p-6">
        <h2 className="text-xl font-semibold">Analyze Security Logs</h2>
        <p className="mt-2 text-sm text-slate-400">
          Select a CSV file to run the backend detection rules.
        </p>

        <input
          type="file"
          accept=".csv,text/csv"
          className="mt-5 block w-full text-sm text-slate-300 file:mr-4 file:rounded-lg file:border-0 file:bg-cyan-300 file:px-4 file:py-2 file:font-semibold file:text-slate-950"
          onChange={(event) => {
            const selected = event.target.files?.[0] ?? null;
            setError("");
            setResult(null);

            if (selected && !selected.name.toLowerCase().endsWith(".csv")) {
              setFile(null);
              setError("Please select a CSV file.");
            } else if (selected && selected.size > MAX_FILE_SIZE) {
              setFile(null);
              setError("Maximum file size is 5 MB.");
            } else {
              setFile(selected);
            }
          }}
        />

        {file && (
          <p className="mt-3 text-sm text-cyan-200">
            Selected: {file.name}
          </p>
        )}

        <button
          type="button"
          onClick={analyzeLogs}
          disabled={!file || loading}
          className="mt-5 rounded-xl bg-cyan-300 px-5 py-3 font-semibold text-slate-950 hover:bg-cyan-200 disabled:cursor-not-allowed disabled:bg-slate-700 disabled:text-slate-400"
        >
          {loading ? "Analyzing..." : "Analyze Logs →"}
        </button>

        {error && (
          <p role="alert" className="mt-4 rounded-lg bg-rose-950 p-4 text-sm text-rose-200">
            {error}
          </p>
        )}
      </section>

      {result && (
        <>
          <section className="mt-8 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
            {[
              ["Total Events", result.summary.total_rows],
              ["Alerts", result.summary.alerts_detected],
              ["Valid Rows", result.summary.valid_rows],
              ["Invalid Rows", result.summary.invalid_rows],
            ].map(([label, value]) => (
              <article
                key={String(label)}
                className="rounded-xl border border-slate-800 bg-[#0d1829] p-5"
              >
                <p className="text-sm text-slate-400">{label}</p>
                <p className="mt-3 text-3xl font-bold text-cyan-200">
                  {value}
                </p>
              </article>
            ))}
          </section>

          <section className="mt-8 overflow-x-auto rounded-2xl border border-slate-800 bg-[#0d1829] p-5">
            <h2 className="mb-4 text-xl font-semibold">Security Alerts</h2>

            {result.alerts.length === 0 ? (
              <p className="text-sm text-slate-400">
                No security alerts detected.
              </p>
            ) : (
              <table className="w-full min-w-[600px] text-left text-sm">
                <thead className="text-slate-400">
                  <tr>
                    <th className="p-3">Rule</th>
                    <th className="p-3">Actor</th>
                    <th className="p-3">Severity</th>
                    <th className="p-3">Details</th>
                  </tr>
                </thead>
                <tbody>
                  {result.alerts.map((alert, index) => (
                    <tr key={index} className="border-t border-slate-800">
                      <td className="p-3">
                        {String(alert.rule_id ?? alert.rule ?? alert.rule_code ?? "—")}
                      </td>
                      <td className="p-3">
                        {String(alert.actor ?? alert.username ?? "—")}
                      </td>
                      <td className="p-3">
                        {String(alert.severity ?? alert.level ?? "—")}
                      </td>
                      <td className="p-3">
                        {String(alert.description ?? alert.message ?? alert.title ?? "Detection triggered")}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </section>

          {result.invalid_rows.length > 0 && (
            <section className="mt-8 rounded-2xl border border-rose-900 bg-[#0d1829] p-5">
              <h2 className="font-semibold text-rose-200">Invalid Rows</h2>
              <pre className="mt-3 overflow-auto whitespace-pre-wrap text-xs text-slate-300">
                {JSON.stringify(result.invalid_rows, null, 2)}
              </pre>
            </section>
          )}
        </>
      )}
    </main>
  );
}