"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
import { Bar, BarChart, CartesianGrid, XAxis, YAxis } from "recharts"

const data = [
  { model: "U-Net", PSNR: 24.6, SSIM: 0.82 },
  { model: "GAN", PSNR: 25.4, SSIM: 0.85 },
  { model: "Diffusion", PSNR: 26.1, SSIM: 0.88 },
]

export function EvaluationCharts() {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-sm">Evaluation</CardTitle>
      </CardHeader>
      <CardContent>
        <ChartContainer
          className="h-64"
          config={{
            PSNR: { label: "PSNR", color: "hsl(var(--chart-2))" },
            SSIM: { label: "SSIM", color: "hsl(var(--chart-1))" },
          }}
        >
          <BarChart data={data}>
            <CartesianGrid strokeOpacity={0.2} vertical={false} />
            <XAxis dataKey="model" tickLine={false} axisLine={false} />
            <YAxis tickLine={false} axisLine={false} />
            <ChartTooltip content={<ChartTooltipContent />} />
            <Bar dataKey="PSNR" fill="var(--color-chart-2)" radius={6} />
            <Bar dataKey="SSIM" fill="var(--color-chart-1)" radius={6} />
          </BarChart>
        </ChartContainer>
      </CardContent>
    </Card>
  )
}
