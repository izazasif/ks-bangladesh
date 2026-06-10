<template>
  <footer class="bg-slate-950 text-slate-300">

    <!-- Main footer content -->
    <div class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid gap-10 md:grid-cols-2 lg:grid-cols-4">

        <!-- Brand -->
        <div class="lg:col-span-1">
          <KSILogo :dark="true" />
          <p class="mt-5 text-sm leading-relaxed text-slate-400">
            KSI Bangladesh is a multi-sector company serving Agriculture, IT, Construction and Transportation across the country since 2010.
          </p>
          <!-- Social icons -->
          <div class="mt-6 flex items-center gap-3">
            <a href="https://www.facebook.com/share/1DhwRxtPxL/" target="_blank" rel="noopener" aria-label="Facebook" class="social-icon">
              <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>
            </a>
            <a href="#" aria-label="LinkedIn" class="social-icon">
              <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
            </a>
            <a href="#" aria-label="Twitter" class="social-icon">
              <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24"><path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"/></svg>
            </a>
            <a href="#" aria-label="YouTube" class="social-icon">
              <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24"><path d="M22.54 6.42a2.78 2.78 0 00-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46a2.78 2.78 0 00-1.95 1.96A29 29 0 001 12a29 29 0 00.46 5.58A2.78 2.78 0 003.41 19.6C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 001.95-1.95A29 29 0 0023 12a29 29 0 00-.46-5.58z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" fill="white"/></svg>
            </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div>
          <h3 class="mb-5 text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Quick Links</h3>
          <ul class="space-y-3 text-sm">
            <li><router-link to="/" class="footer-link">Home</router-link></li>
            <li><router-link to="/about" class="footer-link">About Us</router-link></li>
            <li><router-link to="/services" class="footer-link">Services</router-link></li>
            <li><router-link to="/contact" class="footer-link">Contact Us</router-link></li>
            <li><router-link to="/login" class="footer-link">Login</router-link></li>
            <li><router-link to="/signup" class="footer-link">Sign Up</router-link></li>
          </ul>
        </div>

        <!-- Business Units -->
        <div>
          <h3 class="mb-5 text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Business Unit</h3>
          <ul class="space-y-3 text-sm">
            <li><router-link to="/business-unit/first-class-contractor" class="footer-link">🏗️ First Class Contractor</router-link></li>
            <li><router-link to="/business-unit/supplier" class="footer-link">📦 Supplier</router-link></li>
            <li><router-link to="/business-unit/it" class="footer-link">💻 IT & Technology</router-link></li>
            <li><router-link to="/business-unit/digital-content" class="footer-link">🎬 Digital Content</router-link></li>
            <li><router-link to="/sister-concern/ksi-agricare" class="footer-link">🌾 KSI AgriCare</router-link></li>
            <li><router-link to="/sister-concern/kazi-corporation" class="footer-link">🏢 Kazi Corporation</router-link></li>
            <li><router-link to="/management" class="footer-link">👥 Management</router-link></li>
          </ul>
        </div>

        <!-- Contact info -->
        <div>
          <h3 class="mb-5 text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Contact Us</h3>
          <ul class="space-y-4 text-sm">
            <li class="flex items-start gap-3">
              <span class="mt-0.5 text-base">📍</span>
              <span class="text-slate-400">House/Flat#GA-5/1,5/2, Plot#GA-5/1,5/2, Mohakhali, Banani, Dhaka-1212</span>
            </li>
            <li class="flex items-center gap-3">
              <span class="text-base">📞</span>
              <a href="tel:+8801713266383" class="footer-link">+8801713266383</a>
            </li>
            <li class="flex items-center gap-3">
              <span class="text-base">📞</span>
              <a href="tel:+8801729677233" class="footer-link">+8801729677233</a>
            </li>
            <li class="flex items-center gap-3">
              <span class="text-base">📧</span>
              <a href="mailto:ksibd24@gmail.com" class="footer-link">ksibd24@gmail.com</a>
            </li>
            <li class="flex items-center gap-3">
              <span class="text-base">💬</span>
              <a href="https://wa.me/8801713266383" target="_blank" rel="noopener" class="footer-link">WhatsApp: 01713266383</a>
            </li>
          </ul>
          <router-link to="/contact" class="mt-6 inline-flex rounded-full bg-primary px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-600">
            Get in Touch
          </router-link>
        </div>
      </div>
    </div>

    <!-- Bottom bar -->
    <div class="border-t border-slate-800">
      <div class="mx-auto flex max-w-7xl flex-col items-center justify-between gap-3 px-4 py-5 sm:flex-row sm:px-6 lg:px-8">
        <p class="text-xs text-slate-500">© 2025 KSI Bangladesh. All Rights Reserved.</p>
        <p class="text-xs text-slate-600">Agriculture · IT · Construction · Transportation</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import KSILogo from './KSILogo.vue'</script>

<style scoped>
.footer-link { color: #94a3b8; transition: color 0.15s; }
.footer-link:hover { color: #ffffff; }
.social-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 2rem;
  width: 2rem;
  border-radius: 0.5rem;
  background: rgba(255,255,255,0.08);
  color: #94a3b8;
  transition: background 0.15s, color 0.15s;
}
.social-icon:hover { background: #1A56DB; color: white; }
</style>
