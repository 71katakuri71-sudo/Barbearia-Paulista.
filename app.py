<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Barber.Co — Barbearia Premium</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #111110;
    --surface: #1c1c1a;
    --surface2: #252523;
    --gold: #d4a843;
    --gold-light: #e8bf6a;
    --gold-dark: #a07820;
    --text: #f0ece4;
    --muted: #7a7770;
    --border: rgba(255,255,255,0.07);
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--bg);
    color: var(--text);
    overflow-x: hidden;
  }

  /* NAV */
  nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    display: flex; align-items: center; justify-content: space-between;
    padding: 20px 48px;
    background: rgba(17,17,16,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
    transition: padding 0.3s;
  }
  .logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 28px; letter-spacing: 4px;
    color: var(--text);
  }
  .logo span { color: var(--gold); }
  .nav-links { display: flex; gap: 32px; list-style: none; }
  .nav-links a {
    font-size: 13px; font-weight: 400; letter-spacing: 1.5px;
    text-transform: uppercase; color: var(--muted);
    text-decoration: none; transition: color 0.2s;
  }
  .nav-links a:hover { color: var(--text); }
  .btn-nav {
    font-family: 'DM Sans', sans-serif;
    background: var(--gold); color: #1a1000;
    border: none; border-radius: 4px;
    padding: 10px 22px; font-size: 13px; font-weight: 500;
    letter-spacing: 0.5px; cursor: pointer; transition: background 0.2s;
  }
  .btn-nav:hover { background: var(--gold-light); }

  /* HERO */
  .hero {
    min-height: 100vh;
    display: flex; align-items: center;
    padding: 120px 48px 80px;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute; top: 0; right: 0;
    width: 55%; height: 100%;
    background: linear-gradient(135deg, transparent 30%, rgba(212,168,67,0.04) 100%);
    pointer-events: none;
  }
  .hero-bg-text {
    position: absolute; right: -20px; top: 50%;
    transform: translateY(-50%);
    font-family: 'Bebas Neue', sans-serif;
    font-size: 260px; line-height: 1;
    color: rgba(212,168,67,0.04);
    pointer-events: none; user-select: none;
    letter-spacing: -10px;
  }
  .hero-content { max-width: 580px; position: relative; z-index: 1; }
  .hero-tag {
    display: inline-flex; align-items: center; gap: 8px;
    font-size: 11px; font-weight: 500; letter-spacing: 2px;
    text-transform: uppercase; color: var(--gold);
    margin-bottom: 24px;
  }
  .hero-tag::before {
    content: ''; width: 28px; height: 1px; background: var(--gold);
  }
  .hero h1 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 96px; line-height: 0.9;
    letter-spacing: 2px;
    color: var(--text);
    margin-bottom: 24px;
  }
  .hero h1 em { color: var(--gold); font-style: normal; }
  .hero p {
    font-size: 16px; font-weight: 300; line-height: 1.7;
    color: var(--muted); max-width: 400px; margin-bottom: 40px;
  }
  .hero-btns { display: flex; gap: 14px; align-items: center; margin-bottom: 56px; }
  .btn-primary {
    font-family: 'DM Sans', sans-serif;
    background: var(--gold); color: #1a1000;
    border: none; border-radius: 4px;
    padding: 14px 32px; font-size: 14px; font-weight: 500;
    letter-spacing: 0.5px; cursor: pointer; transition: all 0.2s;
  }
  .btn-primary:hover { background: var(--gold-light); transform: translateY(-1px); }
  .btn-ghost {
    font-family: 'DM Sans', sans-serif;
    background: transparent; color: var(--muted);
    border: 1px solid rgba(255,255,255,0.12); border-radius: 4px;
    padding: 14px 32px; font-size: 14px;
    cursor: pointer; transition: all 0.2s;
  }
  .btn-ghost:hover { color: var(--text); border-color: rgba(255,255,255,0.25); }
  .hero-stats { display: flex; gap: 48px; }
  .stat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 42px; color: var(--gold); line-height: 1;
  }
  .stat-label {
    font-size: 12px; color: var(--muted);
    letter-spacing: 0.5px; margin-top: 2px;
  }
  .stat-divider { width: 1px; background: var(--border); }

  /* SERVICES */
  .services {
    padding: 100px 48px;
    background: var(--surface);
  }
  .section-header { margin-bottom: 56px; }
  .section-tag {
    font-size: 11px; font-weight: 500; letter-spacing: 2px;
    text-transform: uppercase; color: var(--gold);
    margin-bottom: 12px;
  }
  .section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 56px; letter-spacing: 2px; line-height: 1;
  }
  .services-grid {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px;
    background: var(--border);
    border: 1px solid var(--border);
  }
  .svc-card {
    background: var(--surface2);
    padding: 36px 32px;
    position: relative; overflow: hidden;
    transition: background 0.2s;
    cursor: pointer;
  }
  .svc-card:hover { background: #2a2a27; }
  .svc-card.featured { background: #221e10; }
  .svc-card.featured:hover { background: #272214; }
  .svc-badge {
    position: absolute; top: 20px; right: 20px;
    font-size: 10px; font-weight: 500; letter-spacing: 1px;
    text-transform: uppercase; color: #1a1000;
    background: var(--gold); padding: 4px 10px; border-radius: 2px;
  }
  .svc-number {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 72px; color: var(--border);
    line-height: 1; margin-bottom: 20px;
    transition: color 0.2s;
  }
  .svc-card:hover .svc-number,
  .svc-card.featured .svc-number { color: rgba(212,168,67,0.12); }
  .svc-name {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 28px; letter-spacing: 1px;
    margin-bottom: 8px;
  }
  .svc-desc { font-size: 13px; color: var(--muted); line-height: 1.6; margin-bottom: 28px; }
  .svc-footer { display: flex; align-items: flex-end; justify-content: space-between; }
  .svc-price {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 44px; color: var(--gold); line-height: 1;
  }
  .svc-price-label { font-size: 11px; color: var(--muted); margin-bottom: 6px; }
  .svc-time {
    font-size: 12px; color: var(--muted);
    border: 1px solid var(--border); border-radius: 2px;
    padding: 6px 12px; letter-spacing: 0.5px;
  }

  /* BOOKING */
  .booking {
    padding: 100px 48px;
    background: var(--bg);
  }
  .booking-inner {
    display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: start;
  }
  .booking-left .section-tag { margin-bottom: 12px; }
  .booking-left .section-title { margin-bottom: 20px; }
  .booking-left p { font-size: 15px; color: var(--muted); line-height: 1.7; max-width: 360px; }
  .booking-form {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px; padding: 36px;
  }
  .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
  .form-group { display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px; }
  .form-group label {
    font-size: 11px; font-weight: 500; letter-spacing: 1.5px;
    text-transform: uppercase; color: var(--muted);
  }
  .form-group select,
  .form-group input {
    background: var(--surface2); color: var(--text);
    border: 1px solid var(--border); border-radius: 4px;
    padding: 12px 14px; font-size: 14px;
    font-family: 'DM Sans', sans-serif;
    appearance: none; cursor: pointer;
    transition: border-color 0.2s;
  }
  .form-group select:focus,
  .form-group input:focus {
    outline: none; border-color: var(--gold);
  }
  .barbers-row { display: flex; gap: 12px; margin-bottom: 20px; }
  .barber-opt {
    display: flex; flex-direction: column; align-items: center; gap: 6px;
    cursor: pointer;
  }
  .barber-av {
    width: 48px; height: 48px; border-radius: 50%;
    background: var(--surface2);
    border: 2px solid transparent;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; font-weight: 500; color: var(--text);
    transition: border-color 0.2s;
  }
  .barber-opt.active .barber-av,
  .barber-opt:hover .barber-av { border-color: var(--gold); }
  .barber-nm { font-size: 11px; color: var(--muted); }
  .times-grid { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; }
  .time-btn {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px; color: var(--muted);
    background: var(--surface2);
    border: 1px solid var(--border); border-radius: 4px;
    padding: 8px 16px; cursor: pointer; transition: all 0.15s;
  }
  .time-btn:hover:not(:disabled) { color: var(--text); border-color: rgba(255,255,255,0.2); }
  .time-btn.selected { background: var(--gold); color: #1a1000; border-color: var(--gold); font-weight: 500; }
  .time-btn:disabled { opacity: 0.3; cursor: not-allowed; }
  .btn-book {
    width: 100%; font-family: 'DM Sans', sans-serif;
    background: var(--gold); color: #1a1000;
    border: none; border-radius: 4px;
    padding: 15px; font-size: 14px; font-weight: 500;
    letter-spacing: 0.5px; cursor: pointer;
    transition: background 0.2s;
  }
  .btn-book:hover { background: var(--gold-light); }

  /* BARBERS */
  .barbers-section {
    padding: 100px 48px;
    background: var(--surface);
  }
  .barbers-grid {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;
    margin-top: 56px;
  }
  .barber-card {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 32px; text-align: center;
    transition: border-color 0.2s;
  }
  .barber-card:hover { border-color: rgba(212,168,67,0.3); }
  .barber-avatar {
    width: 80px; height: 80px; border-radius: 50%;
    background: var(--gold-dark);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 28px; color: var(--text);
    margin: 0 auto 16px;
    border: 2px solid rgba(212,168,67,0.3);
  }
  .barber-name {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 22px; letter-spacing: 1px; margin-bottom: 4px;
  }
  .barber-role { font-size: 12px; color: var(--muted); letter-spacing: 0.5px; margin-bottom: 16px; }
  .barber-rating { font-size: 13px; color: var(--gold); }

  /* TESTIMONIALS */
  .testimonials {
    padding: 100px 48px;
    background: var(--bg);
  }
  .testi-grid {
    display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;
    margin-top: 56px;
  }
  .testi-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px; padding: 32px;
    position: relative;
  }
  .testi-quote {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 72px; color: rgba(212,168,67,0.15);
    line-height: 0.6; margin-bottom: 16px;
  }
  .testi-text {
    font-size: 15px; font-weight: 300; line-height: 1.7;
    color: #c8c4bc; margin-bottom: 20px;
  }
  .testi-stars { color: var(--gold); font-size: 13px; margin-bottom: 12px; }
  .testi-author { font-size: 13px; font-weight: 500; color: var(--text); }
  .testi-when { font-size: 12px; color: var(--muted); }

  /* FOOTER */
  footer {
    background: var(--surface);
    border-top: 1px solid var(--border);
    padding: 48px;
    display: flex; align-items: center; justify-content: space-between;
  }
  .footer-logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 24px; letter-spacing: 4px; color: var(--text);
  }
  .footer-logo span { color: var(--gold); }
  .footer-links { display: flex; gap: 28px; }
  .footer-links a {
    font-size: 12px; color: var(--muted); text-decoration: none;
    letter-spacing: 0.5px; transition: color 0.2s;
  }
  .footer-links a:hover { color: var(--text); }
  .footer-copy { font-size: 12px; color: var(--muted); }

  /* ANIMATIONS */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  .hero-tag { animation: fadeUp 0.6s ease both; }
  .hero h1 { animation: fadeUp 0.6s 0.1s ease both; }
  .hero p { animation: fadeUp 0.6s 0.2s ease both; }
  .hero-btns { animation: fadeUp 0.6s 0.3s ease both; }
  .hero-stats { animation: fadeUp 0.6s 0.4s ease both; }

  /* RESPONSIVE */
  @media (max-width: 900px) {
    nav { padding: 16px 24px; }
    .nav-links { display: none; }
    .hero { padding: 100px 24px 60px; }
    .hero h1 { font-size: 64px; }
    .hero-bg-text { display: none; }
    .services { padding: 60px 24px; }
    .services-grid { grid-template-columns: 1fr; }
    .booking { padding: 60px 24px; }
    .booking-inner { grid-template-columns: 1fr; gap: 40px; }
    .barbers-section { padding: 60px 24px; }
    .barbers-grid { grid-template-columns: 1fr 1fr; }
    .testimonials { padding: 60px 24px; }
    .testi-grid { grid-template-columns: 1fr; }
    footer { padding: 32px 24px; flex-direction: column; gap: 20px; text-align: center; }
  }
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="logo">BARBER<span>.</span>CO</div>
  <ul class="nav-links">
    <li><a href="#servicos">Serviços</a></li>
    <li><a href="#agendar">Agendar</a></li>
    <li><a href="#barbeiros">Barbeiros</a></li>
    <li><a href="#avaliacoes">Avaliações</a></li>
  </ul>
  <button class="btn-nav" onclick="document.getElementById('agendar').scrollIntoView({behavior:'smooth'})">Agendar agora</button>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-bg-text">BARBER</div>
  <div class="hero-content">
    <div class="hero-tag">Barbearia premium desde 2015</div>
    <h1>SEU<br>ESTILO,<br>DO SEU <em>JEITO</em></h1>
    <p>Cortes clássicos e modernos executados pelos melhores barbeiros da cidade. Agende em segundos, saia impecável.</p>
    <div class="hero-btns">
      <button class="btn-primary" onclick="document.getElementById('agendar').scrollIntoView({behavior:'smooth'})">Agendar horário</button>
      <button class="btn-ghost" onclick="document.getElementById('servicos').scrollIntoView({behavior:'smooth'})">Ver serviços</button>
    </div>
    <div class="hero-stats">
      <div>
        <div class="stat-num">4.9</div>
        <div class="stat-label">Avaliação média</div>
      </div>
      <div class="stat-divider"></div>
      <div>
        <div class="stat-num">800+</div>
        <div class="stat-label">Clientes atendidos</div>
      </div>
      <div class="stat-divider"></div>
      <div>
        <div class="stat-num">10+</div>
        <div class="stat-label">Anos de experiência</div>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="services" id="servicos">
  <div class="section-header">
    <div class="section-tag">O que oferecemos</div>
    <div class="section-title">NOSSOS SERVIÇOS</div>
  </div>
  <div class="services-grid">
    <div class="svc-card">
      <div class="svc-number">01</div>
      <div class="svc-name">Corte Clássico</div>
      <div class="svc-desc">Corte tradicional com acabamento perfeito. Tesoura, máquina e finalização com produtos premium.</div>
      <div class="svc-footer">
        <div>
          <div class="svc-price-label">a partir de</div>
          <div class="svc-price">R$45</div>
        </div>
        <div class="svc-time">30 min</div>
      </div>
    </div>
    <div class="svc-card">
      <div class="svc-number">02</div>
      <div class="svc-name">Barba Completa</div>
      <div class="svc-desc">Aparagem, hidratação e desenho preciso da barba. Toalha quente e produtos artesanais inclusos.</div>
      <div class="svc-footer">
        <div>
          <div class="svc-price-label">a partir de</div>
          <div class="svc-price">R$35</div>
        </div>
        <div class="svc-time">40 min</div>
      </div>
    </div>
    <div class="svc-card featured">
      <div class="svc-badge">Mais pedido</div>
      <div class="svc-number">03</div>
      <div class="svc-name">Corte + Barba</div>
      <div class="svc-desc">Experiência completa. Corte personalizado, barba tratada e finalização com pomada artesanal.</div>
      <div class="svc-footer">
        <div>
          <div class="svc-price-label">a partir de</div>
          <div class="svc-price">R$70</div>
        </div>
        <div class="svc-time">60 min</div>
      </div>
    </div>
  </div>
</section>

<!-- BOOKING -->
<section class="booking" id="agendar">
  <div class="booking-inner">
    <div class="booking-left">
      <div class="section-tag">Reserve seu horário</div>
      <div class="section-title">AGENDAR<br>AGORA</div>
      <p>Escolha o serviço, o barbeiro de preferência e o melhor horário para você. Confirmação imediata via WhatsApp.</p>
    </div>
    <div class="booking-form">
      <div class="form-row">
        <div class="form-group">
          <label>Serviço</label>
          <select>
            <option>Corte clássico — R$45</option>
            <option>Barba completa — R$35</option>
            <option selected>Corte + barba — R$70</option>
          </select>
        </div>
        <div class="form-group">
          <label>Data</label>
          <input type="date" value="2026-04-12">
        </div>
      </div>
      <div class="form-group">
        <label>Barbeiro</label>
        <div class="barbers-row">
          <div class="barber-opt active" onclick="selectBarber(this)">
            <div class="barber-av">JR</div>
            <div class="barber-nm">João</div>
          </div>
          <div class="barber-opt" onclick="selectBarber(this)">
            <div class="barber-av">MR</div>
            <div class="barber-nm">Marco</div>
          </div>
          <div class="barber-opt" onclick="selectBarber(this)">
            <div class="barber-av">LS</div>
            <div class="barber-nm">Lucas</div>
          </div>
          <div class="barber-opt" onclick="selectBarber(this)">
            <div class="barber-av" style="font-size:18px;color:var(--muted)">★</div>
            <div class="barber-nm">Qualquer</div>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label>Horário disponível</label>
        <div class="times-grid">
          <button class="time-btn" onclick="selectTime(this)">09:00</button>
          <button class="time-btn" onclick="selectTime(this)">10:00</button>
          <button class="time-btn selected" onclick="selectTime(this)">11:00</button>
          <button class="time-btn" onclick="selectTime(this)">13:00</button>
          <button class="time-btn" onclick="selectTime(this)">14:00</button>
          <button class="time-btn" disabled>15:00</button>
          <button class="time-btn" onclick="selectTime(this)">16:00</button>
          <button class="time-btn" disabled>17:00</button>
        </div>
      </div>
      <div class="form-group">
        <label>Seu nome</label>
        <input type="text" placeholder="Como podemos te chamar?">
      </div>
      <div class="form-group">
        <label>WhatsApp</label>
        <input type="tel" placeholder="(00) 00000-0000">
      </div>
      <button class="btn-book" onclick="confirmar()">Confirmar agendamento</button>
    </div>
  </div>
</section>

<!-- BARBERS -->
<section class="barbers-section" id="barbeiros">
  <div class="section-tag">Nossa equipe</div>
  <div class="section-title">OS BARBEIROS</div>
  <div class="barbers-grid">
    <div class="barber-card">
      <div class="barber-avatar">JR</div>
      <div class="barber-name">João Rocha</div>
      <div class="barber-role">Master Barber · 8 anos</div>
      <div class="barber-rating">★★★★★ &nbsp; 4.9</div>
    </div>
    <div class="barber-card">
      <div class="barber-avatar">MR</div>
      <div class="barber-name">Marco Reis</div>
      <div class="barber-role">Especialista em Barba · 5 anos</div>
      <div class="barber-rating">★★★★★ &nbsp; 4.8</div>
    </div>
    <div class="barber-card">
      <div class="barber-avatar">LS</div>
      <div class="barber-name">Lucas Silva</div>
      <div class="barber-role">Cortes Modernos · 4 anos</div>
      <div class="barber-rating">★★★★★ &nbsp; 4.9</div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section class="testimonials" id="avaliacoes">
  <div class="section-tag">O que dizem</div>
  <div class="section-title">AVALIAÇÕES</div>
  <div class="testi-grid">
    <div class="testi-card">
      <div class="testi-quote">"</div>
      <div class="testi-stars">★★★★★</div>
      <div class="testi-text">Melhor barbearia da cidade. O João é incrível, sempre sai do jeito que peço. Ambiente top e atendimento impecável.</div>
      <div class="testi-author">Rafael Mendes</div>
      <div class="testi-when">Cliente há 2 anos</div>
    </div>
    <div class="testi-card">
      <div class="testi-quote">"</div>
      <div class="testi-stars">★★★★★</div>
      <div class="testi-text">Agendei pelo site em menos de 1 minuto, chegue no horário e fui atendido na hora. Nunca mais fui em outra barbearia.</div>
      <div class="testi-author">Bruno Santos</div>
      <div class="testi-when">Cliente há 1 ano</div>
    </div>
    <div class="testi-card">
      <div class="testi-quote">"</div>
      <div class="testi-stars">★★★★★</div>
      <div class="testi-text">O corte + barba vale cada centavo. Saí diferente, com a autoestima lá em cima. Recomendo demais.</div>
      <div class="testi-author">Carlos Oliveira</div>
      <div class="testi-when">Cliente há 6 meses</div>
    </div>
    <div class="testi-card">
      <div class="testi-quote">"</div>
      <div class="testi-stars">★★★★★</div>
      <div class="testi-text">Ambiente aconchegante, barbeiros muito profissionais. O Marco fez um trabalho perfeito na minha barba. 10 estrelas!</div>
      <div class="testi-author">Pedro Lima</div>
      <div class="testi-when">Cliente há 3 meses</div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-logo">BARBER<span>.</span>CO</div>
  <div class="footer-links">
    <a href="#">Instagram</a>
    <a href="#">WhatsApp</a>
    <a href="#">Localização</a>
    <a href="#">Contato</a>
  </div>
  <div class="footer-copy">© 2026 Barber.Co — Todos os direitos reservados</div>
</footer>

<script>
  function selectBarber(el) {
    document.querySelectorAll('.barber-opt').forEach(b => b.classList.remove('active'));
    el.classList.add('active');
  }
  function selectTime(el) {
    document.querySelectorAll('.time-btn').forEach(b => b.classList.remove('selected'));
    el.classList.add('selected');
  }
  function confirmar() {
    const nome = document.querySelectorAll('input')[1].value;
    const hora = document.querySelector('.time-btn.selected')?.textContent || '11:00';
    if (!nome.trim()) { alert('Por favor, informe seu nome.'); return; }
    alert('Agendamento confirmado!\n\nHorário: ' + hora + '\nObrigado, ' + nome + '! Você receberá a confirmação pelo WhatsApp em breve.');
  }
  window.addEventListener('scroll', () => {
    const nav = document.querySelector('nav');
    nav.style.padding = window.scrollY > 40 ? '12px 48px' : '20px 48px';
  });
</script>
</body>
</html>
