/* AgriWin Togo — comportements communs (nav mobile, bouton retour en haut, formulaire de contact) */
(function () {
  "use strict";

  /* ---- Navigation mobile ---- */
  var toggle = document.getElementById("navToggle");
  var closeBtn = document.getElementById("navClose");
  var mobileNav = document.getElementById("mobileNav");
  var navIsOpen = false;

  function focusableInNav() {
    return mobileNav.querySelectorAll('a[href], button:not([disabled])');
  }

  function openNav() {
    if (!mobileNav) return;
    navIsOpen = true;
    mobileNav.hidden = false;
    requestAnimationFrame(function () { mobileNav.classList.add("open"); });
    document.body.style.overflow = "hidden";
    if (toggle) toggle.setAttribute("aria-expanded", "true");
    if (closeBtn) closeBtn.focus();
  }
  function closeNav() {
    if (!mobileNav || !navIsOpen) return;
    navIsOpen = false;
    mobileNav.classList.remove("open");
    document.body.style.overflow = "";
    if (toggle) toggle.setAttribute("aria-expanded", "false");
    window.setTimeout(function () { if (!navIsOpen) mobileNav.hidden = true; }, 300);
    if (toggle) toggle.focus();
  }
  if (toggle) toggle.addEventListener("click", openNav);
  if (closeBtn) closeBtn.addEventListener("click", closeNav);
  if (mobileNav) {
    mobileNav.addEventListener("click", function (e) {
      if (e.target === mobileNav) closeNav();
    });
    mobileNav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", closeNav);
    });
  }
  document.addEventListener("keydown", function (e) {
    if (!navIsOpen) return;
    if (e.key === "Escape") { closeNav(); return; }
    if (e.key === "Tab") {
      var focusable = focusableInNav();
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  });

  /* ---- Bouton "retour en haut" ---- */
  var fabTop = document.getElementById("fabTop");
  if (fabTop) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 480) fabTop.classList.add("show");
      else fabTop.classList.remove("show");
    });
    fabTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---- Formulaire de contact (sans backend en Phase 1) ----
     Construit un message pré-rempli et l'envoie soit par WhatsApp,
     soit par e-mail (mailto), au choix du visiteur. */
  var form = document.getElementById("contactForm");
  if (form) {
    var successBox = document.getElementById("formSuccess");

    function buildMessage(data) {
      var lines = [
        "Nouvelle demande depuis le site AgriWin Togo",
        "Nom : " + data.name,
        "Téléphone : " + data.phone,
        data.email ? "E-mail : " + data.email : null,
        "Sujet : " + data.subject,
        "Message : " + data.message,
      ].filter(Boolean);
      return lines.join("\n");
    }

    function getData() {
      return {
        name: form.name.value.trim(),
        phone: form.phone.value.trim(),
        email: form.email.value.trim(),
        subject: form.subject.value,
        message: form.message.value.trim(),
      };
    }

    function validate(data) {
      return data.name && data.phone && data.subject && data.message;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = getData();
      if (!validate(data)) {
        form.reportValidity();
        return;
      }
      var msg = buildMessage(data);
      var action = document.activeElement && document.activeElement.dataset
        ? document.activeElement.dataset.send
        : null;

      if (successBox) {
        successBox.classList.add("show");
        successBox.scrollIntoView({ behavior: "smooth", block: "center" });
      }

      var settings = window.AGRIWIN_SETTINGS || { email: "agriwintogo@gmail.com", phoneDigits: "22896638200" };

      if (action === "email") {
        window.location.href =
          "mailto:" + settings.email + "?subject=" + encodeURIComponent("Demande via le site — " + data.subject) +
          "&body=" + encodeURIComponent(msg);
      } else {
        window.open("https://wa.me/" + settings.phoneDigits + "?text=" + encodeURIComponent(msg), "_blank");
      }
      form.reset();
    });
  }
})();
