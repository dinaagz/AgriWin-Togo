/* @ds-bundle: {"format":4,"namespace":"AgriWin","components":[{"name":"Button"},{"name":"Eyebrow"},{"name":"SectionHead"},{"name":"Card"},{"name":"ServiceCard"},{"name":"ValueCard"},{"name":"ProductCard"},{"name":"StatBand"},{"name":"CtaBand"},{"name":"Field"},{"name":"FilterChip"},{"name":"ContactCard"},{"name":"StepList"},{"name":"Brand"}] } */
/* AgriWin Togo — bibliothèque de composants.
   JavaScript classique, sans dépendance. Chaque fabrique renvoie un élément
   du DOM ; les styles viennent de bundle.css et les couleurs de tokens.css. */
(function () {
  "use strict";

  var ICONS = {
    leaf: 'M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z|M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12',
    school: 'M22 10 12 5 2 10l10 5 10-5Z|M6 12v5c0 1.5 3 3 6 3s6-1.5 6-3v-5',
    users: 'M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2|M23 21v-2a4 4 0 0 0-3-3.87|M16 3.13a4 4 0 0 1 0 7.75',
    shield: 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z',
    target: 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18Z|M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10Z',
    arrow: 'M5 12h14|M12 5l7 7-7 7',
    phone: 'M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z',
    mail: 'M3 5h18v14H3z|M21 6 12 13 3 6',
    pin: 'M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z|M12 13a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z',
    calendar: 'M3 4h18v18H3z|M16 2v4|M8 2v4|M3 10h18',
    check: 'M20 6 9 17l-5-5',
    search: 'M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14Z|M20 20l-4-4'
  };

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  /** Icône trait, 24x24, héritant de la couleur du texte. */
  function Icon(name, size) {
    var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", "2");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");
    svg.setAttribute("aria-hidden", "true");
    if (size) { svg.setAttribute("width", size); svg.setAttribute("height", size); }
    (ICONS[name] || ICONS.leaf).split("|").forEach(function (d) {
      var p = document.createElementNS("http://www.w3.org/2000/svg", "path");
      p.setAttribute("d", d);
      svg.appendChild(p);
    });
    return svg;
  }

  /** Bouton. variant: primary | green | outline | outline-green | call | whatsapp */
  function Button(o) {
    o = o || {};
    var n = el(o.href ? "a" : "button", "aw-btn aw-btn--" + (o.variant || "primary"));
    if (o.size === "sm") n.classList.add("aw-btn--sm");
    if (o.block) n.classList.add("aw-btn--block");
    if (o.href) n.href = o.href; else n.type = o.type || "button";
    if (o.icon) n.appendChild(Icon(o.icon, 18));
    n.appendChild(el("span", null, o.label || "Bouton"));
    if (o.disabled) {
      if (o.href) { n.setAttribute("aria-disabled", "true"); n.removeAttribute("href"); }
      else n.disabled = true;
    }
    if (o.onClick) n.addEventListener("click", o.onClick);
    return n;
  }

  /** Surtitre de section, en capitales. */
  function Eyebrow(o) {
    o = o || {};
    var n = el("span", "aw-eyebrow" + (o.onDark ? " aw-eyebrow--onDark" : ""));
    if (o.icon) n.appendChild(Icon(o.icon, 14));
    n.appendChild(el("span", null, o.label || ""));
    return n;
  }

  /** Titre de section : surtitre, titre, chapô. `accent` met la fin du titre en Playfair. */
  function SectionHead(o) {
    o = o || {};
    var n = el("div", "aw-section-head" + (o.center ? " aw-section-head--center" : ""));
    if (o.eyebrow) n.appendChild(Eyebrow({ label: o.eyebrow, onDark: o.onDark }));
    var h = el("h2");
    h.appendChild(document.createTextNode(o.title || ""));
    if (o.accent) {
      h.appendChild(document.createTextNode(" "));
      h.appendChild(el("span", "aw-accent", o.accent));
    }
    n.appendChild(h);
    if (o.lead) n.appendChild(el("p", null, o.lead));
    return n;
  }

  /** Carte de base : média optionnel, étiquette, titre, texte. */
  function Card(o) {
    o = o || {};
    var n = el("article", "aw-card" + (o.className ? " " + o.className : ""));
    if (o.media) {
      var m = el("div", "aw-card__media");
      var img = el("img");
      img.src = o.media;
      img.alt = o.mediaAlt || "";
      // Différé par défaut : un catalogue peut compter des dizaines de
      // cartes. Passer eagerMedia:true pour une carte visible d'entrée
      // (première ligne d'un catalogue, carte de hero).
      img.loading = o.eagerMedia ? "eager" : "lazy";
      img.decoding = "async";
      m.appendChild(img);
      if (o.badge) m.appendChild(el("span", "aw-product__badge", o.badge));
      n.appendChild(m);
    }
    var b = el("div", "aw-card__body");
    if (o.tag) b.appendChild(el("span", "aw-tag", o.tag));
    if (o.title) b.appendChild(el("h3", null, o.title));
    if (o.text) b.appendChild(el("p", null, o.text));
    (o.children || []).forEach(function (c) { b.appendChild(c); });
    n.appendChild(b);
    return n;
  }

  /** Carte service : pictogramme en dégradé, titre, texte, lien. */
  function ServiceCard(o) {
    o = o || {};
    var n = el("article", "aw-card aw-service");
    var ic = el("div", "aw-icon");
    ic.appendChild(Icon(o.icon || "leaf"));
    n.appendChild(ic);
    n.appendChild(el("h3", null, o.title || ""));
    n.appendChild(el("p", null, o.text || ""));
    if (o.linkLabel) {
      var a = el("a", "aw-service__link");
      a.href = o.href || "#";
      a.appendChild(el("span", null, o.linkLabel));
      a.appendChild(Icon("arrow", 16));
      n.appendChild(a);
    }
    return n;
  }

  /** Carte valeur : pictogramme centré sur fond green-50. */
  function ValueCard(o) {
    o = o || {};
    var n = el("article", "aw-value");
    var ic = el("div", "aw-icon");
    ic.appendChild(Icon(o.icon || "shield"));
    n.appendChild(ic);
    n.appendChild(el("h3", null, o.title || ""));
    n.appendChild(el("p", null, o.text || ""));
    return n;
  }

  /** Carte produit du catalogue : visuel, badge, prix, actions. */
  function ProductCard(o) {
    o = o || {};
    var price = el("div", "aw-product__price");
    price.appendChild(el("strong", null, o.price || ""));
    if (o.unit) price.appendChild(el("span", null, o.unit));
    var actions = el("div", "aw-product__actions");
    actions.appendChild(Button({ label: o.primaryLabel || "Commander", variant: "green", size: "sm" }));
    actions.appendChild(Button({ label: o.secondaryLabel || "Détails", variant: "outline-green", size: "sm" }));
    return Card({
      media: o.media, mediaAlt: o.title, badge: o.badge, tag: o.tag,
      title: o.title, text: o.text, className: "aw-product",
      eagerMedia: o.eagerMedia, children: [price, actions]
    });
  }

  /** Bande de chiffres clés sur dégradé vert. */
  function StatBand(o) {
    o = o || {};
    var n = el("div", "aw-stats");
    (o.items || []).forEach(function (it) {
      var s = el("div", "aw-stat");
      s.appendChild(el("strong", null, it.value));
      s.appendChild(el("span", null, it.label));
      n.appendChild(s);
    });
    n.style.setProperty("--aw-stat-count", (o.items || []).length || 4);
    return n;
  }

  /** Bandeau d'appel à l'action de fin de page. */
  function CtaBand(o) {
    o = o || {};
    var n = el("section", "aw-cta");
    var t = el("div", "aw-cta__text");
    t.appendChild(el("h2", null, o.title || ""));
    if (o.text) t.appendChild(el("p", null, o.text));
    n.appendChild(t);
    var g = el("div", "aw-btn-group");
    (o.actions || []).forEach(function (a) { g.appendChild(Button(a)); });
    n.appendChild(g);
    return n;
  }

  /** Champ de formulaire : libellé, contrôle, aide ou erreur. */
  function Field(o) {
    o = o || {};
    var id = o.id || "aw-" + Math.random().toString(36).slice(2, 8);
    var n = el("div", "aw-field" + (o.error ? " aw-field--error" : ""));
    var l = el("label", null, o.label || "");
    l.htmlFor = id;
    n.appendChild(l);
    var c;
    if (o.as === "textarea") { c = el("textarea"); c.rows = o.rows || 4; }
    else if (o.as === "select") {
      c = el("select");
      (o.options || []).forEach(function (op) {
        var opt = el("option", null, op);
        opt.value = op;
        c.appendChild(opt);
      });
    } else { c = el("input"); c.type = o.type || "text"; }
    c.id = id;
    if (o.placeholder) c.placeholder = o.placeholder;
    if (o.value) c.value = o.value;
    if (o.disabled) c.disabled = true;
    if (o.required) { c.required = true; l.appendChild(el("span", null, " *")); }
    n.appendChild(c);
    // L'aide et l'erreur sont liées au contrôle par aria-describedby : un
    // lecteur d'écran doit entendre pourquoi un champ est invalide, pas
    // seulement qu'il l'est.
    if (o.error) {
      var errId = id + "-error";
      c.setAttribute("aria-invalid", "true");
      c.setAttribute("aria-describedby", errId);
      var errEl = el("span", "aw-field__error", o.error);
      errEl.id = errId;
      errEl.setAttribute("role", "alert");
      n.appendChild(errEl);
    } else if (o.note) {
      var noteId = id + "-note";
      c.setAttribute("aria-describedby", noteId);
      var noteEl = el("span", "aw-field__note", o.note);
      noteEl.id = noteId;
      n.appendChild(noteEl);
    }
    return n;
  }

  /** Puce de filtre du catalogue. */
  function FilterChip(o) {
    o = o || {};
    var n = el("button", "aw-chip", o.label || "");
    n.type = "button";
    n.setAttribute("aria-pressed", o.active ? "true" : "false");
    n.addEventListener("click", function () {
      var on = n.getAttribute("aria-pressed") === "true";
      n.setAttribute("aria-pressed", on ? "false" : "true");
      if (o.onToggle) o.onToggle(!on);
    });
    return n;
  }

  /** Carte de coordonnées sur fond encre de marque. */
  function ContactCard(o) {
    o = o || {};
    var n = el("div", "aw-contact");
    if (o.title) n.appendChild(el("h3", null, o.title));
    (o.lines || []).forEach(function (li) {
      var row = el("div", "aw-contact__line");
      var ic = el("div", "aw-contact__ic");
      ic.appendChild(Icon(li.icon || "phone"));
      row.appendChild(ic);
      var box = el("div");
      box.appendChild(el("strong", null, li.label));
      box.appendChild(el("span", null, li.value));
      row.appendChild(box);
      n.appendChild(row);
    });
    return n;
  }

  /** Liste d'étapes numérotées. */
  function StepList(o) {
    o = o || {};
    // <ol> : un lecteur d'écran annonce nativement « étape 2 sur 4 ». Le
    // cercle numéroté reste, mais en décor (aria-hidden) puisque la liste
    // porte déjà le numéro.
    var n = el("ol", "aw-steps");
    (o.steps || []).forEach(function (s, i) {
      var row = el("li", "aw-step");
      var num = el("div", "aw-step__num", String(i + 1));
      num.setAttribute("aria-hidden", "true");
      row.appendChild(num);
      var box = el("div");
      box.appendChild(el("h3", null, s.title));
      box.appendChild(el("p", null, s.text));
      row.appendChild(box);
      n.appendChild(row);
    });
    return n;
  }

  /** Bloc logo : symbole, nom, signature. */
  function Brand(o) {
    o = o || {};
    var n = el("div", "aw-brand" + (o.onDark ? " aw-brand--onDark" : ""));
    if (o.logo) {
      var img = el("img");
      img.src = o.logo;
      img.alt = "Logo AgriWin Togo";
      n.appendChild(img);
    }
    var t = el("div", "aw-brand__text");
    t.appendChild(el("strong", null, "AgriWin Togo"));
    t.appendChild(el("span", null, "Votre partenaire agricole !"));
    n.appendChild(t);
    return n;
  }

  window.AgriWin = {
    Icon: Icon, Button: Button, Eyebrow: Eyebrow, SectionHead: SectionHead,
    Card: Card, ServiceCard: ServiceCard, ValueCard: ValueCard, ProductCard: ProductCard,
    StatBand: StatBand, CtaBand: CtaBand, Field: Field, FilterChip: FilterChip,
    ContactCard: ContactCard, StepList: StepList, Brand: Brand
  };
})();
