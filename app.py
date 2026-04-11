<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BarberKing – Barbearia Premium</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --gold: #C9A84C;
    --gold-light: #E8CC82;
    --dark: #0D0D0D;
    --dark2: #161616;
    --dark3: #1F1F1F;
    --dark4: #2A2A2A;
    --cream: #F5EFE0;
    --cream2: #EAE0CC;
    --text-muted: #888;
    --text-light: #ccc;
    --red: #C0392B;
  }

  html { scroll-behavior: smooth; }

  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--dark);
    color: var(--cream);
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* ──────────────── NAV ──────────────── */
  nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    display: flex; justify-content: space-between; align-items: center;
    padding: 1.2rem 6%;
    background: rgba(13,13,13,0.92);
    backdrop-filter: blur(8px);
    border-bottom: 1px solid rgba(201,168,76,0.15);
  }

  .logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 900;
    color: var(--gold);
    letter-spacing: 2px;
  }
  .logo span { color: var(--cream); }

  nav ul { list-style: none; display: flex; gap: 2.5rem; }
  nav ul a {
    text-decoration: none; color: var(--text-light);
    font-size: 0.85rem; letter-spacing: 1.5px; text-transform: uppercase;
    font-weight: 500; transition: color 0.2s;
  }
  nav ul a:hover { color: var(--gold); }

  .btn-nav {
    background: var(--gold); color: var(--dark);
    padding: 0.6rem 1.4rem; border: none; border-radius: 2px;
    font-family: 'DM Sans', sans-serif; font-weight: 500;
    font-size: 0.8rem; letter-spacing: 1.5px; text-transform: uppercase;
    cursor: pointer; transition: background 0.2s;
  }
  .btn-nav:hover { background: var(--gold-light); }

  /* ──────────────── HERO ──────────────── */
  #hero {
    min-height: 100vh;
    display: flex; align-items: center;
    padding: 0 6%;
    background:
      linear-gradient(to right, rgba(13,13,13,0.97) 40%, rgba(13,13,13,0.6) 100%),
      url('https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=1400&q=80') center/cover no-repeat;
    position: relative;
  }

  #hero::after {
    content: '';
    position: absolute; left: 0; bottom: 0;
    width: 100%; height: 120px;
    background: linear-gradient(to top, var(--dark), transparent);
  }

  .hero-content { max-width: 580px; z-index: 1; }

  .hero-tag {
    display: inline-block;
    font-size: 0.72rem; letter-spacing: 3px; text-transform: uppercase;
    color: var(--gold); border: 1px solid rgba(201,168,76,0.4);
    padding: 0.35rem 1rem; margin-bottom: 1.5rem;
  }

  .hero-content h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 6vw, 5.5rem);
    font-weight: 900;
    line-height: 1.05;
    margin-bottom: 1.5rem;
  }

  .hero-content h1 em {
    font-style: normal; color: var(--gold);
  }

  .hero-content p {
    font-size: 1.05rem; font-weight: 300; line-height: 1.75;
    color: var(--text-light); margin-bottom: 2.5rem; max-width: 440px;
  }

  .hero-btns { display: flex; gap: 1rem; flex-wrap: wrap; }

  .btn-primary {
    background: var(--gold); color: var(--dark);
    padding: 1rem 2rem; border: none; border-radius: 2px;
    font-family: 'DM Sans', sans-serif; font-weight: 500;
    font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase;
    cursor: pointer; transition: background 0.2s, transform 0.15s;
    text-decoration: none; display: inline-block;
  }
  .btn-primary:hover { background: var(--gold-light); transform: translateY(-1px); }

  .btn-outline {
    background: transparent; color: var(--cream);
    padding: 1rem 2rem; border: 1px solid rgba(245,239,224,0.3); border-radius: 2px;
    font-family: 'DM Sans', sans-serif; font-weight: 400;
    font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase;
    cursor: pointer; transition: border-color 0.2s, color 0.2s;
    text-decoration: none; display: inline-block;
  }
  .btn-outline:hover { border-color: var(--gold); color: var(--gold); }

  /* ──────────────── SERVICES ──────────────── */
  #servicos {
    padding: 7rem 6%;
    background: var(--dark2);
  }

  .section-header { text-align: center; margin-bottom: 4rem; }
  .section-tag {
    display: inline-block; font-size: 0.7rem;
    letter-spacing: 3px; text-transform: uppercase;
    color: var(--gold); margin-bottom: 1rem;
  }
  .section-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 4vw, 3rem); font-weight: 700;
  }
  .section-header p {
    color: var(--text-muted); margin-top: 0.8rem; font-size: 1rem; font-weight: 300;
  }

  .divider {
    width: 50px; height: 2px;
    background: var(--gold); margin: 1.2rem auto 0;
  }

  .services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.5px;
    background: rgba(201,168,76,0.1);
    border: 1px solid rgba(201,168,76,0.1);
  }

  .service-card {
    background: var(--dark2);
    padding: 2.5rem 2rem;
    transition: background 0.2s;
    cursor: default;
  }
  .service-card:hover { background: var(--dark3); }

  .service-icon {
    font-size: 2rem; margin-bottom: 1.2rem; display: block;
  }

  .service-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem; margin-bottom: 0.6rem;
  }

  .service-card p {
    font-size: 0.88rem; color: var(--text-muted); line-height: 1.65; margin-bottom: 1.2rem;
  }

  .service-price {
    font-size: 1.4rem; font-weight: 700; color: var(--gold);
    font-family: 'Playfair Display', serif;
  }
  .service-price span { font-size: 0.75rem; font-weight: 300; color: var(--text-muted); font-family: 'DM Sans', sans-serif; }

  /* ──────────────── TEAM ──────────────── */
  #equipe {
    padding: 7rem 6%;
    background: var(--dark);
  }

  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 2rem;
    margin-top: 1rem;
  }

  .barber-card {
    background: var(--dark3);
    border: 1px solid rgba(201,168,76,0.1);
    overflow: hidden;
    transition: transform 0.2s, border-color 0.2s;
  }
  .barber-card:hover { transform: translateY(-4px); border-color: rgba(201,168,76,0.35); }

  .barber-img {
    width: 100%; height: 280px; object-fit: cover;
    display: block;
    background: var(--dark4);
  }

  .barber-placeholder {
    width: 100%; height: 280px;
    background: linear-gradient(135deg, var(--dark4) 0%, #333 100%);
    display: flex; align-items: center; justify-content: center;
    font-size: 4rem; color: var(--text-muted);
  }

  .barber-info { padding: 1.5rem; }
  .barber-info h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem; margin-bottom: 0.3rem;
  }
  .barber-info .role {
    font-size: 0.78rem; color: var(--gold); letter-spacing: 1.5px;
    text-transform: uppercase; margin-bottom: 0.8rem;
  }
  .barber-info p { font-size: 0.85rem; color: var(--text-muted); line-height: 1.6; }

  /* ──────────────── BOOKING ──────────────── */
  #agendar {
    padding: 7rem 6%;
    background: var(--dark2);
  }

  .booking-wrap {
    display: grid;
    grid-template-columns: 1fr 1.3fr;
    gap: 5rem;
    align-items: start;
  }

  .booking-info h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 3.5vw, 2.8rem); margin-bottom: 1.2rem;
  }

  .booking-info p {
    color: var(--text-muted); line-height: 1.7; font-size: 0.95rem; margin-bottom: 2rem;
  }

  .info-item {
    display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 1.4rem;
  }
  .info-icon {
    width: 40px; height: 40px; min-width: 40px;
    background: rgba(201,168,76,0.1);
    border: 1px solid rgba(201,168,76,0.25);
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
  }
  .info-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 1.5px; color: var(--gold); margin-bottom: 0.2rem; }
  .info-val { font-size: 0.95rem; color: var(--text-light); }

  /* FORM */
  .booking-form {
    background: var(--dark3);
    border: 1px solid rgba(201,168,76,0.12);
    padding: 2.5rem;
  }

  .form-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem; margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(201,168,76,0.1);
  }

  .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }

  .field { margin-bottom: 1.2rem; }

  .field label {
    display: block; font-size: 0.75rem;
    text-transform: uppercase; letter-spacing: 1.5px;
    color: var(--text-muted); margin-bottom: 0.5rem;
  }

  .field input, .field select, .field textarea {
    width: 100%; background: var(--dark);
    border: 1px solid rgba(201,168,76,0.15);
    color: var(--cream); padding: 0.85rem 1rem;
    font-family: 'DM Sans', sans-serif; font-size: 0.95rem;
    border-radius: 0; outline: none;
    transition: border-color 0.2s;
    -webkit-appearance: none;
  }
  .field input:focus, .field select:focus, .field textarea:focus {
    border-color: var(--gold);
  }
  .field select { cursor: pointer; }
  .field select option { background: var(--dark3); }

  .time-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem;
    margin-top: 0.3rem;
  }

  .time-slot {
    padding: 0.6rem; text-align: center;
    background: var(--dark); border: 1px solid rgba(201,168,76,0.15);
    font-size: 0.8rem; cursor: pointer;
    transition: all 0.15s; color: var(--text-light);
    user-select: none;
  }
  .time-slot:hover { border-color: var(--gold); color: var(--gold); }
  .time-slot.selected { background: var(--gold); color: var(--dark); border-color: var(--gold); font-weight: 500; }
  .time-slot.unavailable { opacity: 0.3; cursor: not-allowed; }
  .time-slot.unavailable:hover { border-color: rgba(201,168,76,0.15); color: var(--text-light); }

  .btn-submit {
    width: 100%; background: var(--gold); color: var(--dark);
    padding: 1.1rem; border: none; border-radius: 0;
    font-family: 'DM Sans', sans-serif; font-weight: 500;
    font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase;
    cursor: pointer; margin-top: 1.5rem;
    transition: background 0.2s;
  }
  .btn-submit:hover { background: var(--gold-light); }

  /* SUCCESS */
  .success-msg {
    display: none;
    background: rgba(201,168,76,0.08);
    border: 1px solid rgba(201,168,76,0.3);
    padding: 1.5rem; text-align: center; margin-top: 1.5rem;
  }
  .success-msg .check { font-size: 2rem; margin-bottom: 0.5rem; }
  .success-msg h4 { color: var(--gold); font-family: 'Playfair Display', serif; margin-bottom: 0.4rem; }
  .success-msg p { font-size: 0.88rem; color: var(--text-muted); }

  /* ──────────────── FOOTER ──────────────── */
  footer {
    background: var(--dark);
    border-top: 1px solid rgba(201,168,76,0.1);
    padding: 3rem 6%;
    display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 1rem;
  }
  .footer-logo { font-family: 'Playfair Display', serif; font-size: 1.3rem; color: var(--gold); }
  footer p { font-size: 0.8rem; color: var(--text-muted); }

  /* RESPONSIVE */
  @media (max-width: 900px) {
    .booking-wrap { grid-template-columns: 1fr; gap: 3rem; }
    .form-row { grid-template-columns: 1fr; }
    nav ul { display: none; }
  }
  @media (max-width: 600px) {
    .time-grid { grid-template-columns: repeat(3, 1fr); }
  }
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="logo">BARBER<span>KING</span></div>
  <ul>
    <li><a href="#servicos">Serviços</a></li>
    <li><a href="#equipe">Equipe</a></li>
    <li><a href="#agendar">Agendar</a></li>
  </ul>
  <button class="btn-nav" onclick="document.getElementById('agendar').scrollIntoView({behavior:'smooth'})">Reservar Horário</button>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-content">
    <div class="hero-tag">✦ Barbearia Premium</div>
    <h1>Estilo.<br>Precisão.<br><em>Tradição.</em></h1>
    <p>Mais do que um corte — uma experiência. Cada cliente recebe atenção exclusiva dos nossos mestres barbeiros.</p>
    <div class="hero-btns">
      <a href="#agendar" class="btn-primary">Agendar Agora</a>
      <a href="#servicos" class="btn-outline">Nossos Serviços</a>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section id="servicos">
  <div class="section-header">
    <div class="section-tag">✦ O que oferecemos</div>
    <h2>Serviços</h2>
    <div class="divider"></div>
  </div>
  <div class="services-grid">
    <div class="service-card">
      <span class="service-icon">✂</span>
      <h3>Corte Clássico</h3>
      <p>Corte tradicional com acabamento impecável, adaptado ao seu estilo e formato do rosto.</p>
      <div class="service-price">R$45 <span>/ 40 min</span></div>
    </div>
    <div class="service-card">
      <span class="service-icon">🪒</span>
      <h3>Barba Completa</h3>
      <p>Modelagem, hidratação e acabamento com navalha para uma barba perfeita.</p>
      <div class="service-price">R$40 <span>/ 35 min</span></div>
    </div>
    <div class="service-card">
      <span class="service-icon">👑</span>
      <h3>Combo Premium</h3>
      <p>Corte + barba completa com toalha quente, produtos premium e massagem relaxante.</p>
      <div class="service-price">R$75 <span>/ 70 min</span></div>
    </div>
    <div class="service-card">
      <span class="service-icon">💆</span>
      <h3>Relaxamento Capilar</h3>
      <p>Tratamento profundo para cabelos ressecados ou danificados, com máscara nutritiva.</p>
      <div class="service-price">R$55 <span>/ 50 min</span></div>
    </div>
    <div class="service-card">
      <span class="service-icon">🎨</span>
      <h3>Coloração</h3>
      <p>Coloração moderna ou clássica, incluindo platinado, grisalho e tons naturais.</p>
      <div class="service-price">R$90 <span>/ 90 min</span></div>
    </div>
    <div class="service-card">
      <span class="service-icon">✨</span>
      <h3>Hot Towel Shave</h3>
      <p>Barbear à navalha com 3 toalhas quentes e óleos essenciais. Experiência única.</p>
      <div class="service-price">R$60 <span>/ 45 min</span></div>
    </div>
  </div>
</section>

<!-- TEAM -->
<section id="equipe">
  <div class="section-header">
    <div class="section-tag">✦ Nossos Mestres</div>
    <h2>A Equipe</h2>
    <div class="divider"></div>
  </div>
  <div class="team-grid">
    <div class="barber-card">
      <div class="barber-placeholder">💈</div>
      <div class="barber-info">
        <h3>Carlos Mendonça</h3>
        <div class="role">Master Barber • 12 anos</div>
        <p>Especialista em cortes clássicos e modernos. Referência em degradê e barba estilizada.</p>
      </div>
    </div>
    <div class="barber-card">
      <div class="barber-placeholder">✂</div>
      <div class="barber-info">
        <h3>Rafael Andrade</h3>
        <div class="role">Senior Barber • 8 anos</div>
        <p>Expert em coloração masculina e tratamentos capilares. Criativo e detalhista.</p>
      </div>
    </div>
    <div class="barber-card">
      <div class="barber-placeholder">🪒</div>
      <div class="barber-info">
        <h3>Diego Souza</h3>
        <div class="role">Barbeiro • 5 anos</div>
        <p>Mestre em barbear à navalha e modelagem de barba. Tranquilo e preciso.</p>
      </div>
    </div>
  </div>
</section>

<!-- BOOKING -->
<section id="agendar">
  <div class="booking-wrap">
    <!-- Info -->
    <div class="booking-info">
      <div class="section-tag">✦ Agendamento Online</div>
      <h2>Reserve seu<br><em style="color:var(--gold);font-style:normal">Horário</em></h2>
      <div class="divider" style="margin:1.2rem 0;"></div>
      <p>Escolha o serviço, o barbeiro de sua preferência e o melhor horário para você. Confirmação instantânea por e-mail ou WhatsApp.</p>

      <div class="info-item">
        <div class="info-icon">📍</div>
        <div>
          <div class="info-label">Endereço</div>
          <div class="info-val">Rua das Palmeiras, 142 – Centro<br>Santo Antônio de Jesus, BA</div>
        </div>
      </div>
      <div class="info-item">
        <div class="info-icon">🕐</div>
        <div>
          <div class="info-label">Horário de Funcionamento</div>
          <div class="info-val">Seg – Sex: 9h às 20h<br>Sábado: 8h às 18h</div>
        </div>
      </div>
      <div class="info-item">
        <div class="info-icon">📞</div>
        <div>
          <div class="info-label">Contato</div>
          <div class="info-val">(75) 99999-0000<br>@barberking.saj</div>
        </div>
      </div>
    </div>

    <!-- Form -->
    <div class="booking-form">
      <div class="form-title">✦ Novo Agendamento</div>

      <div class="form-row">
        <div class="field">
          <label>Nome completo</label>
          <input type="text" id="f-nome" placeholder="João Silva">
        </div>
        <div class="field">
          <label>Telefone / WhatsApp</label>
          <input type="tel" id="f-tel" placeholder="(75) 99999-0000">
        </div>
      </div>

      <div class="field">
        <label>Serviço desejado</label>
        <select id="f-servico">
          <option value="">— Selecione —</option>
          <option value="Corte Clássico (R$45)">Corte Clássico – R$45</option>
          <option value="Barba Completa (R$40)">Barba Completa – R$40</option>
          <option value="Combo Premium (R$75)">Combo Premium – R$75</option>
          <option value="Relaxamento Capilar (R$55)">Relaxamento Capilar – R$55</option>
          <option value="Coloração (R$90)">Coloração – R$90</option>
          <option value="Hot Towel Shave (R$60)">Hot Towel Shave – R$60</option>
        </select>
      </div>

      <div class="field">
        <label>Barbeiro</label>
        <select id="f-barbeiro">
          <option value="">— Sem preferência —</option>
          <option value="Carlos Mendonça">Carlos Mendonça</option>
          <option value="Rafael Andrade">Rafael Andrade</option>
          <option value="Diego Souza">Diego Souza</option>
        </select>
      </div>

      <div class="form-row">
        <div class="field">
          <label>Data</label>
          <input type="date" id="f-data" min="">
        </div>
        <div class="field">
          <label>Dia da semana</label>
          <input type="text" id="f-dia" placeholder="—" readonly style="cursor:default;color:var(--text-muted)">
        </div>
      </div>

      <div class="field">
        <label>Horário disponível</label>
        <div class="time-grid" id="time-grid">
          <!-- rendered by JS -->
        </div>
      </div>

      <div id="f-selected-time" style="display:none;margin-top:0.5rem;font-size:0.82rem;color:var(--gold)">✦ Horário selecionado: <span id="f-time-label"></span></div>

      <button class="btn-submit" onclick="submitForm()">Confirmar Agendamento →</button>

      <div class="success-msg" id="success-msg">
        <div class="check">✅</div>
        <h4>Agendamento Confirmado!</h4>
        <p id="success-detail"></p>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-logo">BARBERKING</div>
  <p>© 2025 BarberKing. Todos os direitos reservados.</p>
  <p style="color:var(--gold)">✦ Santo Antônio de Jesus, BA</p>
</footer>

<script>
  // ── Set min date to today
  const today = new Date();
  const yyyy = today.getFullYear();
  const mm = String(today.getMonth()+1).padStart(2,'0');
  const dd = String(today.getDate()).padStart(2,'0');
  document.getElementById('f-data').min = `${yyyy}-${mm}-${dd}`;
  document.getElementById('f-data').value = `${yyyy}-${mm}-${dd}`;

  const diasSemana = ['Domingo','Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado'];

  function updateDia(dateStr) {
    if (!dateStr) return;
    const [y,m,d] = dateStr.split('-').map(Number);
    const dt = new Date(y, m-1, d);
    document.getElementById('f-dia').value = diasSemana[dt.getDay()];
    renderTimeSlots(dt.getDay());
  }

  document.getElementById('f-data').addEventListener('change', e => updateDia(e.target.value));

  // ── Time slots
  const slots = ['08:00','08:30','09:00','09:30','10:00','10:30','11:00','11:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30'];

  let selectedTime = null;

  function renderTimeSlots(dayOfWeek) {
    const grid = document.getElementById('time-grid');
    const isSunday = dayOfWeek === 0;
    const isSaturday = dayOfWeek === 6;

    // Mock some unavailable slots
    const unavailable = ['09:00','10:30','14:00','15:30','17:00'];
    const filtered = slots.filter(s => {
      const h = parseInt(s);
      if (isSunday) return false;
      if (isSaturday && h >= 18) return false;
      return true;
    });

    if (isSunday) {
      grid.innerHTML = '<div style="grid-column:1/-1;text-align:center;color:var(--text-muted);font-size:0.85rem;padding:1rem 0">Fechado aos domingos</div>';
      return;
    }

    grid.innerHTML = filtered.map(t => {
      const ua = unavailable.includes(t) ? 'unavailable' : '';
      return `<div class="time-slot ${ua}" onclick="selectTime(this,'${t}')">${t}</div>`;
    }).join('');
    selectedTime = null;
    document.getElementById('f-selected-time').style.display = 'none';
  }

  function selectTime(el, t) {
    if (el.classList.contains('unavailable')) return;
    document.querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
    el.classList.add('selected');
    selectedTime = t;
    document.getElementById('f-selected-time').style.display = 'block';
    document.getElementById('f-time-label').textContent = t;
  }

  function submitForm() {
    const nome = document.getElementById('f-nome').value.trim();
    const tel = document.getElementById('f-tel').value.trim();
    const servico = document.getElementById('f-servico').value;
    const barbeiro = document.getElementById('f-barbeiro').value;
    const data = document.getElementById('f-data').value;

    if (!nome || !tel || !servico || !data || !selectedTime) {
      alert('Por favor, preencha todos os campos e selecione um horário.');
      return;
    }

    const [y,m,d] = data.split('-').map(Number);
    const dt = new Date(y,m-1,d);
    const dataFormatada = dt.toLocaleDateString('pt-BR',{weekday:'long',day:'2-digit',month:'long'});

    const barb = barbeiro || 'Primeiro disponível';
    document.getElementById('success-detail').textContent =
      `${nome}, você tem um horário com ${barb} para ${servico} no dia ${dataFormatada} às ${selectedTime}.`;

    document.getElementById('success-msg').style.display = 'block';
    document.getElementById('success-msg').scrollIntoView({behavior:'smooth', block:'center'});

    document.getElementById('f-nome').value = '';
    document.getElementById('f-tel').value = '';
    document.getElementById('f-servico').value = '';
    document.getElementById('f-barbeiro').value = '';
    selectedTime = null;
    document.querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
    document.getElementById('f-selected-time').style.display = 'none';
  }

  // Init
  updateDia(document.getElementById('f-data').value);
</script>
</body>
</html>
