export function Footer() {
  return (
    <footer className="mt-8 border-t border-border">
      <div className="mx-auto max-w-7xl px-4 py-8 text-sm text-muted-foreground flex flex-col md:flex-row items-center justify-between gap-3">
        <p>© {new Date().getFullYear()} SAR Colorizer AI. All rights reserved.</p>
        <div className="flex items-center gap-4">
          <a className="hover:underline" href="#" rel="noreferrer">
            GitHub
          </a>
          <a className="hover:underline" href="#" rel="noreferrer">
            Research Paper
          </a>
          <a className="hover:underline" href="mailto:contact@example.com" rel="noreferrer">
            contact@example.com
          </a>
        </div>
      </div>
    </footer>
  )
}
