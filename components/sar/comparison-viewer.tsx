"use client"

import { useMemo, useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Slider } from "@/components/ui/slider"
import Image from "next/image"

type Props = {
  original?: string | null
  colorized?: string | null
  mode?: "split" | "side-by-side"
}

export function ComparisonViewer({ original, colorized, mode = "split" }: Props) {
  const [pos, setPos] = useState(50)
  const hasBoth = useMemo(() => Boolean(original && colorized), [original, colorized])

  return (
    <Card className="h-full">
      <CardHeader>
        <CardTitle className="text-sm">Results Visualization</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {!hasBoth ? (
          <div className="aspect-video w-full rounded-2xl bg-muted/50 border border-dashed grid place-items-center">
            <p className="text-sm text-muted-foreground">Upload an image and run colorization to preview results</p>
          </div>
        ) : mode === "split" ? (
          <div className="relative w-full overflow-hidden rounded-2xl border">
            <Image
              src={original! || "/placeholder.svg"}
              alt="Original SAR"
              width={1280}
              height={720}
              className="w-full h-auto select-none"
              draggable={false}
            />
            <div
              className="absolute top-0 left-0 h-full overflow-hidden pointer-events-none"
              style={{ width: `${pos}%` }}
            >
              <Image
                src={colorized! || "/placeholder.svg"}
                alt="Colorized Output"
                width={1280}
                height={720}
                className="w-full h-auto select-none"
                draggable={false}
              />
            </div>
            <div className="absolute inset-x-0 bottom-3 px-6">
              <Slider value={[pos]} onValueChange={(v) => setPos(v[0]!)} aria-label="Comparison slider" />
            </div>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div className="rounded-2xl border overflow-hidden">
              <Image
                src={original! || "/placeholder.svg"}
                alt="Original SAR"
                width={1280}
                height={720}
                className="w-full h-auto"
              />
            </div>
            <div className="rounded-2xl border overflow-hidden">
              <Image
                src={colorized! || "/placeholder.svg"}
                alt="Colorized Output"
                width={1280}
                height={720}
                className="w-full h-auto"
              />
            </div>
          </div>
        )}
      </CardContent>
    </Card>
  )
}
