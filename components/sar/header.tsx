"use client"

import Image from "next/image"
import Link from "next/link"
import { useTheme } from "next-themes"
import { Button } from "@/components/ui/button"
import { Switch } from "@/components/ui/switch"
import { Separator } from "@/components/ui/separator"

export function Header() {
  const { theme, setTheme } = useTheme()

  return (
    <header className="sticky top-0 z-40 bg-background/80 backdrop-blur supports-[backdrop-filter]:bg-background/60 border-b border-border">
      <div className="mx-auto max-w-7xl px-4 py-3 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <Image
            src="/placeholder-logo.svg"
            width={28}
            height={28}
            alt="SAR Colorizer AI logo"
            className="rounded-md"
          />
          <span className="font-semibold tracking-wide text-pretty">SAR Colorizer AI</span>
        </div>

        <nav className="hidden md:flex items-center gap-2">
          <Button asChild variant="ghost">
            <Link href="#">Home</Link>
          </Button>
          <Button asChild variant="ghost">
            <Link href="#">Model</Link>
          </Button>
          <Button asChild variant="ghost">
            <Link href="#">Results</Link>
          </Button>
          <Button asChild variant="ghost">
            <Link href="#">About</Link>
          </Button>
          <Button asChild variant="ghost">
            <Link href="#">Contact</Link>
          </Button>
        </nav>

        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2">
            <span className="text-xs text-muted-foreground">Light</span>
            <Switch
              aria-label="Toggle dark mode"
              checked={theme !== "light"}
              onCheckedChange={(checked) => setTheme(checked ? "dark" : "light")}
            />
            <span className="text-xs text-muted-foreground">Dark</span>
          </div>
          <Button variant="default" className="bg-primary text-primary-foreground hover:opacity-90">
            Get Started
          </Button>
        </div>
      </div>
      <Separator />
    </header>
  )
}
