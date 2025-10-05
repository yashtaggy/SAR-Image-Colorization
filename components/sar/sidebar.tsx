import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export function Sidebar() {
  return (
    <aside className="space-y-4">
      <Card>
        <CardHeader>
          <CardTitle className="text-sm">Dataset Info</CardTitle>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          <ul className="list-disc pl-5 space-y-1">
            <li>Paired SAR–Optical dataset</li>
            <li>Scenes: Urban, Coastal, Vegetation</li>
            <li>Resolution: 10–30m</li>
            <li>Preprocessing: Speckle reduction, normalization</li>
          </ul>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-sm">Model Insights</CardTitle>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          U-Net encoder-decoder maps SAR features to color space. Optional GAN/Diffusion improve realism with
          adversarial/denoising priors.
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-sm">Usage & Applications</CardTitle>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          Geological analysis, environmental monitoring, and disaster management benefit from enhanced interpretability
          of SAR imagery.
        </CardContent>
      </Card>
    </aside>
  )
}
