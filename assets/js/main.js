(function () {
  "use strict";

  /* ---------------------------------------------------------------- */
  /* Header: solidify on scroll                                       */
  /* ---------------------------------------------------------------- */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (!header) return;
    if (window.scrollY > 40) header.classList.add("is-solid");
    else header.classList.remove("is-solid");
  }
  if (header) { onScroll(); window.addEventListener("scroll", onScroll, { passive: true }); }

  /* ---------------------------------------------------------------- */
  /* Mobile menu                                                       */
  /* ---------------------------------------------------------------- */
  var navToggle = document.querySelector(".nav-toggle");
  var mobileMenu = document.querySelector(".mobile-menu");
  var mobileClose = document.querySelector(".mobile-menu-close");
  function openMenu() { if (mobileMenu) { mobileMenu.classList.add("is-open"); document.body.style.overflow = "hidden"; } }
  function closeMenu() { if (mobileMenu) { mobileMenu.classList.remove("is-open"); document.body.style.overflow = ""; } }
  if (navToggle) navToggle.addEventListener("click", openMenu);
  if (mobileClose) mobileClose.addEventListener("click", closeMenu);

  /* ---------------------------------------------------------------- */
  /* Filter bar (Work index)                                           */
  /* ---------------------------------------------------------------- */
  var filterBar = document.querySelector(".filter-bar");
  if (filterBar) {
    var filterBtns = filterBar.querySelectorAll(".filter-btn");
    var cards = document.querySelectorAll("[data-filter-item]");
    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        var val = btn.getAttribute("data-filter");
        cards.forEach(function (card) {
          var tags = (card.getAttribute("data-filter-item") || "").split(",");
          card.style.display = (val === "all" || tags.indexOf(val) > -1) ? "" : "none";
        });
      });
    });
  }

  /* ---------------------------------------------------------------- */
  /* FAQ accordion                                                      */
  /* ---------------------------------------------------------------- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var q = item.querySelector(".faq-q");
    var a = item.querySelector(".faq-a");
    if (!q || !a) return;
    q.addEventListener("click", function () {
      var isOpen = item.classList.contains("is-open");
      document.querySelectorAll(".faq-item.is-open").forEach(function (openItem) {
        if (openItem !== item) {
          openItem.classList.remove("is-open");
          openItem.querySelector(".faq-a").style.maxHeight = null;
        }
      });
      if (isOpen) { item.classList.remove("is-open"); a.style.maxHeight = null; }
      else { item.classList.add("is-open"); a.style.maxHeight = a.scrollHeight + "px"; }
    });
  });

  /* ---------------------------------------------------------------- */
  /* Lightbox (project galleries)                                       */
  /* ---------------------------------------------------------------- */
  var lightbox = document.querySelector(".lightbox");
  if (lightbox) {
    var lbImgWrap = lightbox.querySelector(".lightbox-img-wrap");
    var lbCaption = lightbox.querySelector(".lightbox-caption");
    var triggers = Array.prototype.slice.call(document.querySelectorAll("[data-lightbox-trigger]"));
    var current = 0;
    function renderLb() {
      var t = triggers[current];
      lbImgWrap.innerHTML = t.querySelector(".ph-block") ? t.querySelector(".ph-block").outerHTML : "";
      lbCaption.textContent = t.getAttribute("data-caption") || "";
    }
    function openLb(i) { current = i; renderLb(); lightbox.classList.add("is-open"); document.body.style.overflow = "hidden"; }
    function closeLb() { lightbox.classList.remove("is-open"); document.body.style.overflow = ""; }
    triggers.forEach(function (t, i) { t.addEventListener("click", function (e) { e.preventDefault(); openLb(i); }); });
    var closeBtn = lightbox.querySelector(".lightbox-close");
    var prevBtn = lightbox.querySelector(".lightbox-prev");
    var nextBtn = lightbox.querySelector(".lightbox-next");
    if (closeBtn) closeBtn.addEventListener("click", closeLb);
    if (prevBtn) prevBtn.addEventListener("click", function () { current = (current - 1 + triggers.length) % triggers.length; renderLb(); });
    if (nextBtn) nextBtn.addEventListener("click", function () { current = (current + 1) % triggers.length; renderLb(); });
    lightbox.addEventListener("click", function (e) { if (e.target === lightbox) closeLb(); });
    document.addEventListener("keydown", function (e) {
      if (!lightbox.classList.contains("is-open")) return;
      if (e.key === "Escape") closeLb();
      if (e.key === "ArrowRight" && nextBtn) nextBtn.click();
      if (e.key === "ArrowLeft" && prevBtn) prevBtn.click();
    });
  }

  /* ---------------------------------------------------------------- */
  /* Client gallery password gate (demo only — not real security)      */
  /* ---------------------------------------------------------------- */
  var gateForm = document.querySelector("[data-gate-form]");
  if (gateForm) {
    gateForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var input = gateForm.querySelector("input[name=access_code]");
      var errorEl = gateForm.querySelector(".field-error");
      if (input && input.value.trim().length > 0) {
        document.querySelector(".password-gate").style.display = "none";
        document.querySelector("[data-gate-content]").style.display = "";
      } else if (errorEl) {
        errorEl.style.display = "block";
      }
    });
  }

  /* ---------------------------------------------------------------- */
  /* Generic form "submit" simulation (Contact, etc. — no real backend) */
  /* ---------------------------------------------------------------- */
  document.querySelectorAll("[data-demo-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var success = form.querySelector(".form-success");
      if (success) { success.classList.add("is-visible"); form.reset(); success.scrollIntoView({ behavior: "smooth", block: "center" }); }
    });
  });

  /* ---------------------------------------------------------------- */
  /* Client onboarding — multi-step Part A + Part B, Netlify Forms    */
  /* ---------------------------------------------------------------- */
  var onbForm = document.querySelector("[data-onb-form]");
  if (onbForm) {
    var ONB_KEY = "lari_onboarding_v1";
    var steps = Array.prototype.slice.call(onbForm.querySelectorAll(".onb-step"));
    var navBtns = Array.prototype.slice.call(document.querySelectorAll(".onb-nav-btn"));
    var prevBtn = onbForm.querySelector("[data-onb-prev]");
    var nextBtn = onbForm.querySelector("[data-onb-next]");
    var submitBtn = onbForm.querySelector("[data-onb-submit]");
    var errorBox = onbForm.querySelector("[data-onb-error]");
    var bar = document.querySelector("[data-onb-bar]");
    var progressText = document.querySelector("[data-onb-progress-text]");
    var total = steps.length;
    var saved = {};
    try { saved = JSON.parse(localStorage.getItem(ONB_KEY)) || {}; } catch (e) { saved = {}; }
    var state = saved.values || {};
    var visited = saved.visited || [1];
    var current = 1;

    function persist() {
      try { localStorage.setItem(ONB_KEY, JSON.stringify({ values: state, visited: visited, step: current })); } catch (e) {}
    }

    function readField(el) {
      if (el.type === "file" || el.name === "bot-field" || el.name === "form-name") return;
      if (el.type === "checkbox" && el.closest(".onb-group")) {
        state[el.name] = Array.prototype.slice.call(onbForm.querySelectorAll('input[name="' + el.name + '"]:checked')).map(function (i) { return i.value; });
      } else if (el.type === "checkbox") {
        state[el.name] = el.checked ? el.value : "";
      } else if (el.type === "radio") {
        if (el.checked) state[el.name] = el.value;
      } else {
        state[el.name] = el.value;
      }
    }

    // Restore saved answers
    Array.prototype.forEach.call(onbForm.elements, function (el) {
      if (!el.name || !(el.name in state) || el.type === "file") return;
      var v = state[el.name];
      if (el.type === "checkbox" || el.type === "radio") {
        el.checked = Array.isArray(v) ? v.indexOf(el.value) > -1 : v === el.value;
      } else { el.value = v; }
    });

    onbForm.addEventListener("input", function (e) { if (e.target.name) { readField(e.target); clearError(e.target); persist(); } });
    onbForm.addEventListener("change", function (e) { if (e.target.name) { readField(e.target); clearError(e.target); persist(); } });

    function clearError(el) {
      var wrap = el.closest(".field");
      if (wrap) wrap.classList.remove("has-error");
    }

    function validateStep(n) {
      var step = steps[n - 1], firstBad = null;
      step.querySelectorAll(".field").forEach(function (wrap) {
        var bad = false;
        if (wrap.hasAttribute("data-required-group")) {
          bad = !wrap.querySelector("input:checked");
        } else {
          var el = wrap.querySelector("input[required], select[required], textarea[required]");
          if (el) bad = el.type === "checkbox" ? !el.checked : (!el.value.trim() || !el.checkValidity());
          var opt = wrap.querySelector("input[type=email]:not([required]), input[type=url]:not([required])");
          if (opt && opt.value && !opt.checkValidity()) bad = true;
          var file = wrap.querySelector("input[type=file]");
          if (file && file.files[0] && file.files[0].size > 8 * 1024 * 1024) bad = true;
        }
        wrap.classList.toggle("has-error", bad);
        if (bad && !firstBad) firstBad = wrap;
      });
      return firstBad;
    }

    function isStepComplete(n) {
      var ok = true;
      steps[n - 1].querySelectorAll("[required]").forEach(function (el) {
        if (el.type === "checkbox" ? !el.checked : !el.value.trim()) ok = false;
      });
      steps[n - 1].querySelectorAll("[data-required-group]").forEach(function (g) { if (!g.querySelector("input:checked")) ok = false; });
      return ok;
    }

    function escHtml(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

    function renderReview() {
      var out = "";
      steps.slice(0, -1).forEach(function (step, i) {
        var rows = "";
        step.querySelectorAll(".field").forEach(function (wrap) {
          var labelEl = wrap.querySelector("legend, label");
          var label = labelEl ? labelEl.textContent.replace(/\*\s*$/, "").trim() : "";
          var el = wrap.querySelector("input, select, textarea");
          if (!el) return;
          var v;
          if (el.type === "file") v = el.files[0] ? el.files[0].name : "";
          else if (wrap.classList.contains("onb-group")) v = [].concat(state[el.name] || []).join(", ");
          else if (el.type === "checkbox") { v = el.checked ? "Agreed" : ""; label = label.length > 70 ? label.slice(0, 70) + "…" : label; }
          else v = el.value;
          rows += "<dt>" + escHtml(label) + "</dt><dd" + (v ? "" : ' class="is-empty"') + ">" + (v ? escHtml(v) : "Not provided") + "</dd>";
        });
        out += '<div class="onb-review-block"><div class="onb-review-head"><div><small>' + escHtml(step.getAttribute("data-part")) + "</small><h4>" + escHtml(step.getAttribute("data-step-title")) + '</h4></div><button type="button" class="btn btn-ghost btn-sm" data-goto="' + (i + 1) + '">Edit</button></div><dl>' + rows + "</dl></div>";
      });
      onbForm.querySelector("[data-onb-review]").innerHTML = out;
    }

    function go(n, focus) {
      n = Math.max(1, Math.min(total, n));
      current = n;
      if (visited.indexOf(n) === -1) visited.push(n);
      steps.forEach(function (s, i) { s.hidden = i !== n - 1; });
      navBtns.forEach(function (b) {
        var t = +b.getAttribute("data-goto");
        b.classList.toggle("is-current", t === n);
        b.classList.toggle("is-done", t !== n && t < total && visited.indexOf(t) > -1 && isStepComplete(t));
        if (t === n) b.setAttribute("aria-current", "step"); else b.removeAttribute("aria-current");
      });
      prevBtn.style.visibility = n === 1 ? "hidden" : "visible";
      nextBtn.hidden = n === total;
      submitBtn.hidden = n !== total;
      errorBox.hidden = true;
      if (n === total) renderReview();
      var pct = Math.round(((n - 1) / (total - 1)) * 100);
      bar.style.width = pct + "%";
      progressText.textContent = "Step " + n + " of " + total + " — " + steps[n - 1].getAttribute("data-step-title") + " · " + pct + "% complete";
      if (location.hash !== "#step-" + n) history.replaceState(null, "", "#step-" + n);
      persist();
      if (focus !== false) {
        var top = document.querySelector(".onb-progress").getBoundingClientRect().top + window.scrollY - 110;
        if (window.scrollY > top) window.scrollTo({ top: top, behavior: "smooth" });
        var h = steps[n - 1].querySelector("h2"); h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true });
      }
    }

    document.addEventListener("click", function (e) {
      var t = e.target.closest("[data-goto]");
      if (t && document.querySelector(".onb-layout").contains(t)) { e.preventDefault(); go(+t.getAttribute("data-goto")); }
    });
    prevBtn.addEventListener("click", function () { go(current - 1); });
    nextBtn.addEventListener("click", function () {
      var bad = validateStep(current);
      if (bad) { var f = bad.querySelector("input, select, textarea"); if (f) f.focus(); bad.scrollIntoView({ behavior: "smooth", block: "center" }); return; }
      go(current + 1);
    });

    onbForm.addEventListener("submit", function (e) {
      e.preventDefault();
      for (var i = 1; i < total; i++) {
        if (validateStep(i)) {
          go(i);
          errorBox.textContent = "A few required answers are missing in \"" + steps[i - 1].getAttribute("data-step-title") + "\". They're highlighted below.";
          errorBox.hidden = false;
          return;
        }
      }
      submitBtn.disabled = true;
      submitBtn.textContent = "Submitting…";
      fetch("/", { method: "POST", body: new FormData(onbForm) })
        .then(function (res) {
          if (!res.ok) throw new Error("HTTP " + res.status);
          try { localStorage.removeItem(ONB_KEY); } catch (err) {}
          history.replaceState(null, "", location.pathname);
          document.querySelector(".onb-layout").classList.add("is-complete");
          document.querySelector(".onb-nav").hidden = true;
          onbForm.hidden = true;
          document.querySelector("[data-onb-done]").hidden = false;
          bar.style.width = "100%";
          progressText.textContent = "Onboarding complete";
          window.scrollTo({ top: 0, behavior: "smooth" });
        })
        .catch(function () {
          errorBox.textContent = "Something went wrong sending your onboarding. Please try again, or email us if it keeps happening.";
          errorBox.hidden = false;
          submitBtn.disabled = false;
          submitBtn.textContent = "Submit Onboarding";
        });
    });

    var fromHash = parseInt((location.hash.match(/^#step-(\d+)$/) || [])[1], 10);
    go(fromHash || saved.step || 1, false);
  }

  /* ---------------------------------------------------------------- */
  /* LARI ACADEMY — front-end-only auth + LMS demo, backed by          */
  /* localStorage. No real backend: see README for what a production   */
  /* build needs (Supabase/Firebase/Auth0 + a database).                */
  /* ---------------------------------------------------------------- */
  var LS_USERS = "lari_academy_users";
  var LS_SESSION = "lari_academy_session";

  function getUsers() { try { return JSON.parse(localStorage.getItem(LS_USERS)) || {}; } catch (e) { return {}; } }
  function saveUsers(u) { localStorage.setItem(LS_USERS, JSON.stringify(u)); }
  function getSession() { return localStorage.getItem(LS_SESSION); }
  function setSession(email) { localStorage.setItem(LS_SESSION, email); }
  function clearSession() { localStorage.removeItem(LS_SESSION); }

  // Pre-seed a demo account (idempotent) so reviewers can see a populated
  // dashboard without registering first: demo@laricreativestudio.com / demo1234
  (function seedDemoAccount() {
    var users = getUsers();
    if (!users["demo@laricreativestudio.com"]) {
      users["demo@laricreativestudio.com"] = {
        name: "Demo Student",
        email: "demo@laricreativestudio.com",
        password: "demo1234",
        enrolled: [
          { slug: "brand-strategy-identity-design", title: "Brand Strategy & Identity Design", progress: 60, paid: true, currency: "ngn", amount: "₦35,000", enrolledOn: new Date().toISOString() },
          { slug: "ui-ux-fundamentals", title: "UI/UX Design Fundamentals", progress: 100, paid: true, currency: "usd", amount: "$45", enrolledOn: new Date().toISOString() },
          { slug: "ai-automation-for-business", title: "AI Automation for Business", progress: 20, paid: true, currency: "gbp", amount: "£37", enrolledOn: new Date().toISOString() },
        ],
        purchasedGuides: [
          { slug: "starter", title: "Starter — Get the Complete Guide", currency: "ngn", amount: "₦12,000", purchasedOn: new Date().toISOString() },
        ],
        created: new Date().toISOString(),
      };
      saveUsers(users);
    }
  })();

  function nextRedirectTarget() {
    // ?next=course:<slug> or ?next=guide:<key> — sends the user back to where
    // they clicked "buy" so they can complete payment now that they're signed in.
    var params = new URLSearchParams(window.location.search);
    var next = params.get("next");
    if (!next) return relPrefix() + "academy/dashboard/";
    var parts = next.split(":");
    if (parts[0] === "course" && parts[1]) return relPrefix() + "academy/courses/" + parts[1] + "/";
    if (parts[0] === "guide") return relPrefix() + "academy/#courses";
    return relPrefix() + "academy/dashboard/";
  }

  // Registration
  var registerForm = document.querySelector("[data-academy-register]");
  if (registerForm) {
    registerForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var errorBox = registerForm.querySelector(".auth-error");
      var name = registerForm.querySelector("[name=full_name]").value.trim();
      var email = registerForm.querySelector("[name=email]").value.trim().toLowerCase();
      var password = registerForm.querySelector("[name=password]").value;
      if (!name || !email || password.length < 6) {
        errorBox.textContent = "Please fill in every field — password needs at least 6 characters.";
        errorBox.classList.add("is-visible");
        return;
      }
      var users = getUsers();
      if (users[email]) {
        errorBox.textContent = "An account with that email already exists — try signing in instead.";
        errorBox.classList.add("is-visible");
        return;
      }
      users[email] = { name: name, email: email, password: password, enrolled: [], purchasedGuides: [], created: new Date().toISOString() };
      saveUsers(users);
      setSession(email);
      window.location.href = nextRedirectTarget();
    });
  }

  // Sign in
  var signinForm = document.querySelector("[data-academy-signin]");
  if (signinForm) {
    signinForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var errorBox = signinForm.querySelector(".auth-error");
      var email = signinForm.querySelector("[name=email]").value.trim().toLowerCase();
      var password = signinForm.querySelector("[name=password]").value;
      var users = getUsers();
      if (!users[email] || users[email].password !== password) {
        errorBox.textContent = "We couldn't match that email and password. Try again, or register a new account.";
        errorBox.classList.add("is-visible");
        return;
      }
      setSession(email);
      window.location.href = nextRedirectTarget();
    });
  }

  // ---------------------------------------------------------------- */
  // Payment modal (demo checkout) — gates course/guide access behind a
  // one-time "payment" so nothing is accessible until it's confirmed.
  // Real currency conversion / processing is NOT implemented: this is a
  // static-site demo. See README for what a production build needs
  // (Paystack/Flutterwave for NGN, Stripe for USD/GBP/EUR, etc).
  // ---------------------------------------------------------------- */
  var paymentModal = document.querySelector(".payment-modal");
  if (paymentModal) {
    var pmTitle = paymentModal.querySelector("[data-pm-title]");
    var pmAmount = paymentModal.querySelector("[data-pm-amount]");
    var pmCurrency = paymentModal.querySelector("[data-pm-currency]");
    var pmConfirm = paymentModal.querySelector("[data-pm-confirm]");
    var pmClose = paymentModal.querySelector(".payment-modal-close");
    var pmActiveBtn = null;

    function pmPriceFor(btn, currency) {
      return btn.getAttribute("data-buy-" + currency) || "";
    }
    function pmRefreshAmount() {
      if (!pmActiveBtn) return;
      pmAmount.textContent = pmPriceFor(pmActiveBtn, pmCurrency.value);
    }
    function openPaymentModal(btn) {
      pmActiveBtn = btn;
      pmTitle.textContent = btn.getAttribute("data-buy-title") || "Item";
      pmCurrency.value = "ngn";
      pmRefreshAmount();
      paymentModal.classList.add("is-open");
      paymentModal.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
    }
    function closePaymentModal() {
      paymentModal.classList.remove("is-open");
      paymentModal.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
      pmActiveBtn = null;
    }

    document.querySelectorAll("[data-buy-type]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var email = getSession();
        var type = btn.getAttribute("data-buy-type");
        var slug = btn.getAttribute("data-buy-slug");
        if (!email) {
          window.location.href = relPrefix() + "academy/signin/?next=" + encodeURIComponent(type + ":" + slug);
          return;
        }
        openPaymentModal(btn);
      });
    });

    pmCurrency.addEventListener("change", pmRefreshAmount);
    if (pmClose) pmClose.addEventListener("click", closePaymentModal);
    paymentModal.addEventListener("click", function (e) { if (e.target === paymentModal) closePaymentModal(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && paymentModal.classList.contains("is-open")) closePaymentModal(); });

    pmConfirm.addEventListener("click", function () {
      if (!pmActiveBtn) return;
      var email = getSession();
      if (!email) { closePaymentModal(); return; }
      var type = pmActiveBtn.getAttribute("data-buy-type");
      var slug = pmActiveBtn.getAttribute("data-buy-slug");
      var title = pmActiveBtn.getAttribute("data-buy-title");
      var currency = pmCurrency.value;
      var amount = pmPriceFor(pmActiveBtn, currency);
      var users = getUsers();
      var user = users[email];
      if (!user) { closePaymentModal(); return; }

      if (type === "course") {
        if (!user.enrolled) user.enrolled = [];
        if (!user.enrolled.some(function (c) { return c.slug === slug; })) {
          user.enrolled.push({ slug: slug, title: title, progress: 0, paid: true, currency: currency, amount: amount, enrolledOn: new Date().toISOString() });
        }
        saveUsers(users);
        closePaymentModal();
        window.location.href = relPrefix() + "academy/dashboard/my-courses.html";
      } else if (type === "guide") {
        if (!user.purchasedGuides) user.purchasedGuides = [];
        if (!user.purchasedGuides.some(function (g) { return g.slug === slug; })) {
          user.purchasedGuides.push({ slug: slug, title: title, currency: currency, amount: amount, purchasedOn: new Date().toISOString() });
        }
        saveUsers(users);
        closePaymentModal();
        pmActiveBtn.textContent = "Purchased — check your email (demo)";
        pmActiveBtn.setAttribute("disabled", "disabled");
        pmActiveBtn.classList.add("is-disabled");
      }
    });
  }

  // Dashboard guard + render (any element with [data-dash-page])
  var dashPage = document.querySelector("[data-dash-page]");
  if (dashPage) {
    var email = getSession();
    var users = getUsers();
    var user = email ? users[email] : null;
    if (!user) {
      window.location.href = relPrefix() + "academy/signin/";
    } else {
      document.querySelectorAll("[data-user-name]").forEach(function (el) { el.textContent = user.name; });
      document.querySelectorAll("[data-user-email]").forEach(function (el) { el.textContent = user.email; });
      var enrolled = user.enrolled || [];

      // Overview stats
      var statTotal = document.querySelector("[data-stat-total]");
      var statInProgress = document.querySelector("[data-stat-inprogress]");
      var statDone = document.querySelector("[data-stat-done]");
      if (statTotal) statTotal.textContent = enrolled.length;
      if (statInProgress) statInProgress.textContent = enrolled.filter(function (c) { return c.progress > 0 && c.progress < 100; }).length;
      if (statDone) statDone.textContent = enrolled.filter(function (c) { return c.progress >= 100; }).length;

      // My courses list
      var listEl = document.querySelector("[data-enrolled-list]");
      if (listEl) {
        if (enrolled.length === 0) {
          listEl.innerHTML = '<div class="empty-state"><h3>No courses yet</h3><p>Browse the Academy, pay for a course, and it will appear here.</p><a class="btn btn-primary" href="' + relPrefix() + 'academy/">Browse courses</a></div>';
        } else {
          listEl.innerHTML = enrolled.map(function (c, i) {
            var paidNote = c.paid ? '<div class="enrol-track">Paid ' + (c.amount || "") + '</div>' : '<div class="enrol-track">In progress</div>';
            return '<div class="enrol-row">' +
              '<div><div class="enrol-title">' + c.title + '</div>' + paidNote + '</div>' +
              '<div><div class="progress-track"><div class="progress-fill" style="width:' + c.progress + '%"></div></div><div class="progress-pct">' + c.progress + '% complete</div></div>' +
              '<button class="btn btn-sm btn-ghost" data-advance="' + i + '">Log study session (+20%)</button>' +
              '</div>';
          }).join("");
          listEl.querySelectorAll("[data-advance]").forEach(function (btn) {
            btn.addEventListener("click", function () {
              var idx = parseInt(btn.getAttribute("data-advance"), 10);
              var fresh = getUsers();
              var u2 = fresh[email];
              u2.enrolled[idx].progress = Math.min(100, u2.enrolled[idx].progress + 20);
              saveUsers(fresh);
              window.location.reload();
            });
          });
        }
      }

      // Purchased guides (Core Guide bundle)
      var guidesEl = document.querySelector("[data-guides-list]");
      if (guidesEl) {
        var guides = user.purchasedGuides || [];
        if (guides.length === 0) {
          guidesEl.innerHTML = '<div class="empty-state"><h3>No guides purchased yet</h3><p>The Core Guide is available from the Academy page.</p></div>';
        } else {
          guidesEl.innerHTML = guides.map(function (g) {
            return '<div class="enrol-row"><div><div class="enrol-title">' + g.title + '</div><div class="enrol-track">Paid ' + (g.amount || "") + '</div></div><span class="badge">Purchased</span></div>';
          }).join("");
        }
      }

      // Certificates
      var certEl = document.querySelector("[data-cert-list]");
      if (certEl) {
        var done = enrolled.filter(function (c) { return c.progress >= 100; });
        if (done.length === 0) {
          certEl.innerHTML = '<div class="empty-state"><h3>No certificates yet</h3><p>Complete a course to earn its certificate here.</p></div>';
        } else {
          certEl.innerHTML = done.map(function (c) {
            return '<div class="cert-card"><div><div class="cert-card-name">' + c.title + '</div><div class="cert-card-date">Completed</div></div><span class="badge">Certified</span></div>';
          }).join("");
        }
      }

      // Logout
      document.querySelectorAll("[data-logout]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          clearSession();
          window.location.href = relPrefix() + "academy/";
        });
      });
    }
  }

  // If already signed in, redirect away from register/signin pages
  if ((registerForm || signinForm) && getSession()) {
    // Only redirect if the user is actually mid-flow on those pages
  }
})();
