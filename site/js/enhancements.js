/* =========================================================
   AgriWin Togo — Micro-interactions et animations au scroll
   Progressif : rien de bloquant, tout dégrade proprement si
   IntersectionObserver n'est pas disponible.
   ========================================================= */
(function () {
  "use strict";

  var prefersReduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Barre de progression de lecture en haut ---------- */
  var progress = document.createElement("div");
  progress.className = "scroll-progress";
  document.body.appendChild(progress);

  /* ---------- Header qui rétrécit au scroll ---------- */
  var header = document.querySelector(".site-header");

  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      var scrolled = window.scrollY;
      var pct = docHeight > 0 ? (scrolled / docHeight) * 100 : 0;
      progress.style.width = pct + "%";
      if (header) header.classList.toggle("is-scrolled", scrolled > 8);
      ticking = false;
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Révélation au scroll (auto-tag des sections) ---------- */
  if ("IntersectionObserver" in window && !prefersReduced) {
    // Cibles à révéler automatiquement : .section-head, .card, .service-photo-card, .value-card,
    // .portrait-quote, .mood-item, .two-col > *, .cta-band, .stats-band > *, .steps > .step
    var selectors = [
      ".section .section-head",
      ".section .grid > *",
      ".section .two-col > *",
      ".section .stats-band > *",
      ".section .steps > .step",
      ".section .portrait-quote",
      ".section .mood-gallery > *",
      ".section .cta-band",
      ".section .img-frame",
      ".section .values-grid > *",
      ".section .catalogue-toolbar",
      ".section .filter-chips",
      ".photo-band .photo-band-content",
    ];
    var targets = document.querySelectorAll(selectors.join(","));

    // Attribue un délai en cascade à l'intérieur d'un même parent (max 6)
    var perParent = new WeakMap();
    Array.prototype.forEach.call(targets, function (el) {
      el.classList.add("reveal");
      var parent = el.parentElement;
      var count = perParent.get(parent) || 0;
      if (count > 0 && count <= 6) el.setAttribute("data-delay", count);
      perParent.set(parent, count + 1);
    });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });

    Array.prototype.forEach.call(targets, function (el) { io.observe(el); });

    // Hero : classe is-visible pour lancer le zoom-out doux
    var heroes = document.querySelectorAll(".photo-hero");
    Array.prototype.forEach.call(heroes, function (h) {
      requestAnimationFrame(function () { h.classList.add("is-visible"); });
    });
  } else {
    // Pas d'IO ou motion réduit : on affiche tout tout de suite
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---------- Comptage animé des statistiques ---------- */
  if ("IntersectionObserver" in window && !prefersReduced) {
    var statEls = document.querySelectorAll(".stats-band .stat-item strong");
    var statTargets = [];
    Array.prototype.forEach.call(statEls, function (el) {
      var match = el.textContent.match(/^(\d[\d\s]*)(.*)$/);
      if (!match) return; // valeur non numérique (ex. "Togo") : pas d'animation
      var value = parseInt(match[1].replace(/\s/g, ""), 10);
      if (isNaN(value)) return;
      el.dataset.suffix = match[2];
      el.dataset.target = value;
      el.textContent = "0" + match[2];
      statTargets.push(el);
    });

    function animateCount(el) {
      var target = parseInt(el.dataset.target, 10);
      var suffix = el.dataset.suffix || "";
      var duration = 1400;
      var start = null;
      function step(ts) {
        if (start === null) start = ts;
        var progress = Math.min((ts - start) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(eased * target) + suffix;
        if (progress < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }

    if (statTargets.length) {
      var statIo = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateCount(entry.target);
            statIo.unobserve(entry.target);
          }
        });
      }, { threshold: 0.4 });
      statTargets.forEach(function (el) { statIo.observe(el); });
    }
  }

  /* ---------- Effet de survol "magnétique" léger sur les boutons principaux ---------- */
  if (!prefersReduced && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    var magnetic = document.querySelectorAll(".btn-primary, .btn-green, .btn-whatsapp");
    Array.prototype.forEach.call(magnetic, function (btn) {
      btn.addEventListener("mousemove", function (e) {
        var rect = btn.getBoundingClientRect();
        var x = e.clientX - rect.left - rect.width / 2;
        var y = e.clientY - rect.top - rect.height / 2;
        btn.style.transform = "translate(" + x * 0.12 + "px, " + (y * 0.12 - 2) + "px)";
      });
      btn.addEventListener("mouseleave", function () {
        btn.style.transform = "";
      });
    });
  }

  /* ---------- Nav mobile : verrouille le scroll quand ouvert ---------- */
  var mobileNav = document.getElementById("mobileNav");
  if (mobileNav) {
    var lockObserver = new MutationObserver(function () {
      var open = mobileNav.classList.contains("open");
      document.documentElement.style.overflow = open ? "hidden" : "";
    });
    lockObserver.observe(mobileNav, { attributes: true, attributeFilter: ["class"] });
  }
})();
