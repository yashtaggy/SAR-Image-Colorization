"use client"

import { useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Progress } from "@/components/ui/progress"
import { Spinner } from "@/components/ui/spinner"

type Props = {
  model: string
  setModel: (m: string) => void
  onRun: () => void
  progress: number
  processing: boolean
  disabled: boolean
}

export function ProcessingPanel({ model, setModel, onRun, progress, processing, disabled }: Props) {
  useEffect(() => {
    // no-op: visual component only
  }, [])

  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-sm">Processing</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="space-y-2">
          <Label htmlFor="model">Model Version</Label>
          <Select value={model} onValueChange={setModel}>
            <SelectTrigger id="model" className="w-full">
              <SelectValue placeholder="Select model" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="unet">U-Net</SelectItem>
              <SelectItem value="gan">GAN</SelectItem>
              <SelectItem value="diffusion">Diffusion</SelectItem>
            </SelectContent>
          </Select>
        </div>

        <Button
          onClick={onRun}
          disabled={disabled || processing}
          className="w-full bg-accent text-accent-foreground hover:opacity-90"
        >
          {processing ? (
            <span className="inline-flex items-center gap-2">
              <Spinner className="size-4" /> Running…
            </span>
          ) : (
            "Run Colorization"
          )}
        </Button>

        <div className="space-y-2">
          <div className="flex items-center justify-between text-xs">
            <span className="text-muted-foreground">Progress</span>
            <span className="tabular-nums">{Math.floor(progress)}%</span>
          </div>
          <Progress value={progress} />
        </div>
      </CardContent>
    </Card>
  )
}
