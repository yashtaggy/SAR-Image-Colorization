"use client"

import { useCallback, useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"

type Props = {
  onFileSelected: (file: File, url: string) => void
  onClear: () => void
}

export function UploadDropzone({ onFileSelected, onClear }: Props) {
  const [dragOver, setDragOver] = useState(false)

  const handleFiles = useCallback(
    (files: FileList | null) => {
      if (!files || !files[0]) return
      const file = files[0]
      if (!/\.(tif|tiff|png|jpg|jpeg)$/i.test(file.name)) return
      const url = URL.createObjectURL(file)
      onFileSelected(file, url)
    },
    [onFileSelected],
  )

  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-sm">Upload SAR Image</CardTitle>
      </CardHeader>
      <CardContent>
        <div
          className={[
            "rounded-2xl border-2 border-dashed p-6 text-center transition-colors",
            dragOver ? "border-primary bg-primary/5" : "border-border",
          ].join(" ")}
          onDragOver={(e) => {
            e.preventDefault()
            setDragOver(true)
          }}
          onDragLeave={() => setDragOver(false)}
          onDrop={(e) => {
            e.preventDefault()
            setDragOver(false)
            handleFiles(e.dataTransfer.files)
          }}
        >
          <p className="text-sm text-muted-foreground mb-3">Drag & drop your grayscale SAR image (.tif, .png)</p>
          <div className="flex items-center justify-center gap-2">
            <label className="inline-flex items-center gap-2">
              <Input
                type="file"
                accept=".tif,.tiff,.png,.jpg,.jpeg"
                className="hidden"
                onChange={(e) => handleFiles(e.target.files)}
              />
              <Button variant="default" className="bg-primary text-primary-foreground">
                Upload
              </Button>
            </label>
            <Button variant="secondary" onClick={onClear}>
              Clear
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
