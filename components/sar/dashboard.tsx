"use client"

import { useCallback, useMemo, useState } from "react"
import { Sidebar } from "./sidebar"
import { UploadDropzone } from "./upload-dropzone"
import { ProcessingPanel } from "./processing-panel"
import { ComparisonViewer } from "./comparison-viewer"
import { MetricsPanel } from "./metrics-panel"
import { EvaluationCharts } from "./evaluation-charts"
import { Card, CardContent } from "@/components/ui/card"

type Metrics = {
  psnr?: number
  ssim?: number
  confidence?: number
}

export function Dashboard() {
  const [file, setFile] = useState<File | null>(null)
  const [originalUrl, setOriginalUrl] = useState<string | null>(null)
  const [colorizedUrl, setColorizedUrl] = useState<string | null>(null)
  const [processing, setProcessing] = useState(false)
  const [progress, setProgress] = useState(0)
  const [model, setModel] = useState<string>("unet")
  const [metrics, setMetrics] = useState<Metrics>({})

  const clearAll = useCallback(() => {
    setFile(null)
    if (originalUrl) URL.revokeObjectURL(originalUrl)
    if (colorizedUrl) URL.revokeObjectURL(colorizedUrl)
    setOriginalUrl(null)
    setColorizedUrl(null)
    setProgress(0)
    setProcessing(false)
    setMetrics({})
  }, [originalUrl, colorizedUrl])

  const onFileSelected = useCallback((f: File, url: string) => {
    setFile(f)
    setOriginalUrl(url)
    setColorizedUrl(null)
    setProgress(0)
    setMetrics({})
  }, [])

  const runColorization = useCallback(() => {
    if (!file || processing) return
    setProcessing(true)
    setProgress(0)

    // Simulate inference progress
    const start = Date.now()
    const totalMs = 2200
    const t = setInterval(() => {
      const elapsed = Date.now() - start
      const pct = Math.min(100, (elapsed / totalMs) * 100)
      setProgress(pct)
      if (pct >= 100) {
        clearInterval(t)
        // "Generate" colorized image: for demo reuse the original (in real app, replace with model output)
        setColorizedUrl(originalUrl)
        // Fake metrics vary by model
        const base = model === "diffusion" ? 26.1 : model === "gan" ? 25.4 : 24.6
        const ssim = model === "diffusion" ? 0.88 : model === "gan" ? 0.85 : 0.82
        setMetrics({ psnr: base, ssim, confidence: 0.92 })
        setProcessing(false)
      }
    }, 100)
  }, [file, processing, originalUrl, model])

  const disabled = useMemo(() => !file, [file])

  return (
    <section className="mx-auto max-w-7xl px-4 py-6">
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left: Sidebar */}
        <div className="lg:col-span-3">
          <Sidebar />
        </div>

        {/* Center: Upload + Visualization */}
        <div className="lg:col-span-6 space-y-4">
          <UploadDropzone onFileSelected={onFileSelected} onClear={clearAll} />
          <Card>
            <CardContent className="p-4">
              <ComparisonViewer original={originalUrl ?? undefined} colorized={colorizedUrl ?? undefined} />
            </CardContent>
          </Card>
          <EvaluationCharts />
        </div>

        {/* Right: Controls + Metrics */}
        <div className="lg:col-span-3 space-y-4">
          <ProcessingPanel
            model={model}
            setModel={setModel}
            onRun={runColorization}
            progress={progress}
            processing={processing}
            disabled={disabled}
          />
          <MetricsPanel metrics={metrics} colorizedUrl={colorizedUrl ?? undefined} />
        </div>
      </div>
    </section>
  )
}
