"use client"

import { useMemo } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip"

type Metrics = {
  psnr?: number
  ssim?: number
  confidence?: number
}

type Props = {
  metrics: Metrics
  colorizedUrl?: string | null
}

export function MetricsPanel({ metrics, colorizedUrl }: Props) {
  const canDownload = useMemo(() => Boolean(colorizedUrl), [colorizedUrl])

  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-sm">Metrics & Download</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <TooltipProvider>
          <div className="grid grid-cols-3 gap-3">
            <Metric
              label="PSNR"
              value={metrics.psnr ? `${metrics.psnr.toFixed(2)} dB` : "—"}
              hint="Peak Signal-to-Noise Ratio: higher is better"
            />
            <Metric
              label="SSIM"
              value={metrics.ssim ? metrics.ssim.toFixed(3) : "—"}
              hint="Structural Similarity Index: 0–1, higher is better"
            />
            <Metric
              label="Confidence"
              value={metrics.confidence ? `${Math.round(metrics.confidence * 100)}%` : "—"}
              hint="Model confidence score for the current output"
            />
          </div>
        </TooltipProvider>

        <Button className="w-full bg-primary text-primary-foreground hover:opacity-90" asChild disabled={!canDownload}>
          <a href={colorizedUrl ?? "#"} download="colorized.png" aria-disabled={!canDownload}>
            Download Colorized Image
          </a>
        </Button>
      </CardContent>
    </Card>
  )
}

function Metric({ label, value, hint }: { label: string; value: string; hint: string }) {
  return (
    <Tooltip>
      <TooltipTrigger asChild>
        <div className="rounded-xl border p-3 text-center">
          <div className="text-xs text-muted-foreground">{label}</div>
          <div className="text-lg font-semibold tabular-nums">{value}</div>
        </div>
      </TooltipTrigger>
      <TooltipContent>{hint}</TooltipContent>
    </Tooltip>
  )
}
