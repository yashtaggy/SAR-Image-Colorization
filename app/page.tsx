import { Header } from "@/components/sar/header"
import { Footer } from "@/components/sar/footer"
import { Dashboard } from "@/components/sar/dashboard"

export default function Page() {
  return (
    <main className="min-h-screen">
      <Header />
      <Dashboard />
      <Footer />
    </main>
  )
}
