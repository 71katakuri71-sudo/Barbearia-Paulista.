<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Navalha & Co. — Barbearia</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --black: #0d0d0d;
    --cream: #f5f0e8;
    --gold: #c9a84c;
    --gold-light: #e8d08a;
    --dark: #1a1a1a;
    --mid: #2e2e2e;
    --text-muted: #888;
    --danger: #c0392b;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--black);
    color: var(--cream);
    overflow-x: hidden;
    cursor: default;
  }

  /* ─── NAV ─── */
  nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    display: flex; align-items: center; justify-content: space-between;
    padding: 1.2rem 3rem;
    background: rgba(13,13,13,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(201,168,76,0.2);
  }
  .nav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem; font-weight: 900; letter-spacing: 0.05em;
    color: var(--gold);
    text-decoration: none;
  }
  .nav-links { display: flex; gap: 2rem; }
  .nav-links a {
    color: var(--cream); text-decoration: none;
    font-size: 0.85rem; letter-spacing: 0.1em; text-transform: uppercase;
    opacity: 0.8; transition: opacity 0.2s, color 0.2s;
  }
  .nav-links a:hover { opacity: 1; color: var(--gold); }
  #btn-barbeiro-nav {
    background: none; border: 1px solid var(--gold);
    color: var(--gold); padding: 0.4rem 1rem; border-radius: 2px;
    cursor: pointer; font-size: 0.75rem; letter-spacing: 0.1em;
    text-transform: uppercase; transition: all 0.2s; font-family: 'DM Sans', sans-serif;
  }
  #btn-barbeiro-nav:hover { background: var(--gold); color: var(--black); }

  /* ─── HERO ─── */
  #home {
    min-height: 100vh; display: flex; align-items: center;
    position: relative; overflow: hidden;
    background: linear-gradient(135deg, #0d0d0d 0%, #1a1208 50%, #0d0d0d 100%);
  }
  .hero-bg {
    position: absolute; inset: 0;
    background-image:
      radial-gradient(ellipse 60% 60% at 70% 50%, rgba(201,168,76,0.08) 0%, transparent 70%),
      repeating-linear-gradient(45deg, transparent, transparent 40px, rgba(201,168,76,0.02) 40px, rgba(201,168,76,0.02) 41px);
  }
  .hero-line {
    position: absolute; left: 3rem; top: 0; bottom: 0;
    width: 1px; background: linear-gradient(to bottom, transparent, var(--gold), transparent);
    opacity: 0.3;
  }
  .hero-content {
    position: relative; z-index: 1;
    padding: 8rem 3rem 4rem 6rem;
    max-width: 700px;
  }
  .hero-eyebrow {
    font-size: 0.75rem; letter-spacing: 0.3em; text-transform: uppercase;
    color: var(--gold); margin-bottom: 1.5rem;
    display: flex; align-items: center; gap: 1rem;
  }
  .hero-eyebrow::before {
    content: ''; width: 40px; height: 1px; background: var(--gold);
  }
  .hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 7vw, 5.5rem);
    line-height: 1.05; font-weight: 900;
    margin-bottom: 1.5rem;
  }
  .hero-title em { font-style: italic; color: var(--gold); }
  .hero-subtitle {
    font-size: 1rem; color: rgba(245,240,232,0.6);
    line-height: 1.8; max-width: 440px; margin-bottom: 3rem;
    font-weight: 300;
  }
  .hero-cta {
    display: inline-flex; align-items: center; gap: 1rem;
    background: var(--gold); color: var(--black);
    padding: 1rem 2.5rem; font-size: 0.85rem;
    letter-spacing: 0.15em; text-transform: uppercase;
    font-weight: 500; cursor: pointer; border: none;
    transition: all 0.3s; font-family: 'DM Sans', sans-serif;
    text-decoration: none;
  }
  .hero-cta:hover { background: var(--gold-light); transform: translateX(4px); }
  .hero-cta::after { content: '→'; font-size: 1rem; }
  .hero-number {
    position: absolute; right: 4rem; top: 50%;
    transform: translateY(-50%);
    font-family: 'Playfair Display', serif;
    font-size: 12rem; font-weight: 900;
    color: rgba(201,168,76,0.04);
    user-select: none; line-height: 1;
  }

  /* ─── SECTIONS ─── */
  section { padding: 6rem 3rem; }
  .section-label {
    font-size: 0.7rem; letter-spacing: 0.4em; text-transform: uppercase;
    color: var(--gold); margin-bottom: 1rem;
    display: flex; align-items: center; gap: 0.8rem;
  }
  .section-label::after { content: ''; flex: 1; max-width: 40px; height: 1px; background: var(--gold); }
  .section-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 4vw, 3rem); font-weight: 700;
    margin-bottom: 1rem;
  }

  /* ─── SERVIÇOS ─── */
  #servicos { background: var(--dark); }
  .services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1px; margin-top: 3rem;
    border: 1px solid rgba(201,168,76,0.15);
  }
  .service-card {
    padding: 2.5rem 2rem;
    border-right: 1px solid rgba(201,168,76,0.15);
    transition: background 0.3s;
    position: relative; overflow: hidden;
  }
  .service-card:last-child { border-right: none; }
  .service-card::before {
    content: ''; position: absolute; bottom: 0; left: 0; right: 0;
    height: 2px; background: var(--gold);
    transform: scaleX(0); transform-origin: left;
    transition: transform 0.3s;
  }
  .service-card:hover::before { transform: scaleX(1); }
  .service-card:hover { background: rgba(201,168,76,0.05); }
  .service-icon { font-size: 1.8rem; margin-bottom: 1rem; }
  .service-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem; margin-bottom: 0.5rem;
  }
  .service-desc { font-size: 0.85rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 1rem; }
  .service-price { font-size: 1.3rem; color: var(--gold); font-weight: 500; }
  .service-duration { font-size: 0.75rem; color: var(--text-muted); margin-left: 0.5rem; }

  /* ─── AGENDAMENTO ─── */
  #agendar {
    background: var(--black);
    display: flex; gap: 4rem; align-items: flex-start;
    flex-wrap: wrap;
  }
  .agendar-info { flex: 1; min-width: 280px; }
  .agendar-form-wrap { flex: 1.4; min-width: 320px; }
  .form-card {
    background: var(--dark);
    border: 1px solid rgba(201,168,76,0.2);
    padding: 2.5rem;
  }
  .form-group { margin-bottom: 1.5rem; }
  .form-group label {
    display: block; font-size: 0.75rem; letter-spacing: 0.15em;
    text-transform: uppercase; color: var(--gold);
    margin-bottom: 0.6rem;
  }
  .form-group input, .form-group select {
    width: 100%; padding: 0.9rem 1rem;
    background: var(--mid); border: 1px solid rgba(201,168,76,0.2);
    color: var(--cream); font-family: 'DM Sans', sans-serif;
    font-size: 0.95rem; outline: none; transition: border-color 0.2s;
    -webkit-appearance: none;
  }
  .form-group input:focus, .form-group select:focus {
    border-color: var(--gold);
  }
  .form-group select option { background: var(--dark); }
  .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }

  /* horários */
  .horarios-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem;
    margin-top: 0.6rem;
  }
  .horario-btn {
    padding: 0.6rem 0; font-size: 0.8rem;
    background: var(--mid); border: 1px solid rgba(201,168,76,0.15);
    color: var(--cream); cursor: pointer; transition: all 0.2s;
    font-family: 'DM Sans', sans-serif;
  }
  .horario-btn:hover { border-color: var(--gold); color: var(--gold); }
  .horario-btn.selected { background: var(--gold); color: var(--black); border-color: var(--gold); }
  .horario-btn.ocupado { opacity: 0.3; cursor: not-allowed; text-decoration: line-through; }

  .btn-submit {
    width: 100%; padding: 1.1rem;
    background: var(--gold); color: var(--black);
    border: none; cursor: pointer; font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem; font-weight: 500; letter-spacing: 0.1em;
    text-transform: uppercase; transition: all 0.2s; margin-top: 0.5rem;
  }
  .btn-submit:hover { background: var(--gold-light); }

  /* ─── INFO BARBEARIA ─── */
  .info-list { margin-top: 2rem; }
  .info-item {
    display: flex; align-items: flex-start; gap: 1rem;
    padding: 1.2rem 0; border-bottom: 1px solid rgba(245,240,232,0.08);
  }
  .info-item:last-child { border-bottom: none; }
  .info-icon { font-size: 1.1rem; margin-top: 0.1rem; }
  .info-label { font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.1em; }
  .info-val { font-size: 0.95rem; margin-top: 0.2rem; line-height: 1.6; }

  /* ─── FOOTER ─── */
  footer {
    background: var(--dark);
    border-top: 1px solid rgba(201,168,76,0.15);
    padding: 2rem 3rem;
    display: flex; align-items: center; justify-content: space-between;
    flex-wrap: wrap; gap: 1rem;
    font-size: 0.8rem; color: var(--text-muted);
  }
  .footer-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem; color: var(--gold); font-weight: 700;
  }

  /* ─── MODAL / OVERLAY ─── */
  .overlay {
    display: none; position: fixed; inset: 0; z-index: 200;
    background: rgba(0,0,0,0.85); backdrop-filter: blur(6px);
    align-items: center; justify-content: center;
  }
  .overlay.active { display: flex; }
  .modal {
    background: var(--dark);
    border: 1px solid rgba(201,168,76,0.3);
    width: 100%; max-width: 440px;
    padding: 2.5rem; position: relative;
    animation: slideUp 0.3s ease;
  }
  @keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
  .modal-close {
    position: absolute; top: 1rem; right: 1.2rem;
    background: none; border: none; color: var(--text-muted);
    font-size: 1.3rem; cursor: pointer; line-height: 1;
    transition: color 0.2s;
  }
  .modal-close:hover { color: var(--cream); }
  .modal-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem; margin-bottom: 0.4rem;
  }
  .modal-sub { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 2rem; }
  .modal-input {
    width: 100%; padding: 0.9rem 1rem; margin-bottom: 1rem;
    background: var(--mid); border: 1px solid rgba(201,168,76,0.2);
    color: var(--cream); font-family: 'DM Sans', sans-serif; font-size: 0.95rem;
    outline: none; transition: border-color 0.2s;
  }
  .modal-input:focus { border-color: var(--gold); }
  .modal-btn {
    width: 100%; padding: 1rem;
    background: var(--gold); color: var(--black);
    border: none; cursor: pointer; font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem; font-weight: 500; letter-spacing: 0.1em;
    text-transform: uppercase; transition: background 0.2s;
  }
  .modal-btn:hover { background: var(--gold-light); }
  .modal-error { font-size: 0.82rem; color: #e74c3c; margin-top: 0.5rem; display: none; }

  /* ─── PAINEL DO BARBEIRO — NOVO DASHBOARD ─── */
  #painel {
    display: none; min-height: 100vh;
    background: #111;
  }
  #painel.active { display: flex; flex-direction: column; }

  /* sidebar + main layout */
  .dash-layout { display: flex; flex: 1; min-height: 100vh; }

  .dash-sidebar {
    width: 240px; flex-shrink: 0;
    background: #0d0d0d;
    border-right: 1px solid rgba(201,168,76,0.12);
    display: flex; flex-direction: column;
    padding: 2rem 0;
    position: sticky; top: 0; height: 100vh; overflow-y: auto;
  }
  .sidebar-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem; color: var(--gold); font-weight: 900;
    padding: 0 1.5rem 2rem;
    border-bottom: 1px solid rgba(201,168,76,0.1);
    margin-bottom: 1.5rem;
  }
  .sidebar-logo small { display: block; font-family: 'DM Sans', sans-serif; font-size: 0.7rem; color: var(--text-muted); font-weight: 400; margin-top: 0.2rem; letter-spacing: 0.1em; text-transform: uppercase; }
  .sidebar-nav { flex: 1; }
  .sidebar-item {
    display: flex; align-items: center; gap: 0.8rem;
    padding: 0.85rem 1.5rem; font-size: 0.85rem;
    color: var(--text-muted); cursor: pointer;
    border-left: 2px solid transparent;
    transition: all 0.2s; user-select: none;
  }
  .sidebar-item:hover { color: var(--cream); background: rgba(201,168,76,0.04); }
  .sidebar-item.active { color: var(--gold); border-left-color: var(--gold); background: rgba(201,168,76,0.06); }
  .sidebar-item .s-icon { font-size: 1rem; width: 20px; text-align: center; }
  .sidebar-footer {
    padding: 1.5rem;
    border-top: 1px solid rgba(201,168,76,0.1);
  }
  .btn-sair {
    width: 100%; padding: 0.6rem;
    background: none; border: 1px solid rgba(192,57,43,0.3);
    color: #c0392b; cursor: pointer; font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem; letter-spacing: 0.1em; text-transform: uppercase;
    transition: all 0.2s;
  }
  .btn-sair:hover { background: rgba(192,57,43,0.1); }

  /* main content */
  .dash-main { flex: 1; overflow-y: auto; }
  .dash-topbar {
    padding: 1.5rem 2.5rem;
    border-bottom: 1px solid rgba(201,168,76,0.1);
    display: flex; align-items: center; justify-content: space-between;
    background: #111; position: sticky; top: 0; z-index: 10;
  }
  .dash-topbar-title { font-family: 'Playfair Display', serif; font-size: 1.3rem; }
  .dash-topbar-date { font-size: 0.8rem; color: var(--text-muted); }
  .badge-live {
    display: inline-flex; align-items: center; gap: 0.4rem;
    font-size: 0.68rem; font-family: 'DM Sans', sans-serif;
    background: rgba(201,168,76,0.1); color: var(--gold);
    padding: 0.25rem 0.8rem; letter-spacing: 0.1em; text-transform: uppercase;
  }
  .badge-live::before { content:''; width:6px; height:6px; background:var(--gold); border-radius:50%; animation: blink 1.5s infinite; }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.2} }

  .dash-content { padding: 2rem 2.5rem; }

  /* views */
  .dash-view { display: none; }
  .dash-view.active { display: block; }

  /* KPI cards */
  .kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem; margin-bottom: 2rem;
  }
  .kpi-card {
    background: #1a1a1a;
    border: 1px solid rgba(201,168,76,0.12);
    padding: 1.4rem 1.5rem;
    position: relative; overflow: hidden;
    transition: border-color 0.2s;
  }
  .kpi-card:hover { border-color: rgba(201,168,76,0.3); }
  .kpi-card::after {
    content: ''; position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
    background: var(--gold); opacity: 0;
    transition: opacity 0.2s;
  }
  .kpi-card:hover::after { opacity: 1; }
  .kpi-icon { font-size: 1.3rem; margin-bottom: 1rem; }
  .kpi-val { font-family: 'Playfair Display', serif; font-size: 2rem; color: var(--cream); line-height: 1; }
  .kpi-val span { font-size: 1rem; color: var(--gold); margin-left: 2px; }
  .kpi-label { font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.4rem; }
  .kpi-change { font-size: 0.72rem; margin-top: 0.6rem; }
  .kpi-change.up { color: #27ae60; }
  .kpi-change.neutral { color: var(--text-muted); }

  /* timeline de hoje */
  .timeline-section { margin-bottom: 2rem; }
  .section-head {
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 1rem;
  }
  .section-head h3 { font-family: 'Playfair Display', serif; font-size: 1.1rem; }
  .timeline { display: flex; flex-direction: column; gap: 0.6rem; }
  .timeline-item {
    display: flex; align-items: center; gap: 1rem;
    background: #1a1a1a; border: 1px solid rgba(201,168,76,0.1);
    padding: 1rem 1.2rem; transition: border-color 0.2s;
    position: relative;
  }
  .timeline-item:hover { border-color: rgba(201,168,76,0.25); }
  .tl-hora {
    font-family: 'Playfair Display', serif;
    font-size: 1rem; color: var(--gold); min-width: 52px; font-weight: 700;
  }
  .tl-divider { width: 1px; height: 36px; background: rgba(201,168,76,0.2); }
  .tl-info { flex: 1; }
  .tl-nome { font-size: 0.92rem; font-weight: 500; }
  .tl-serv { font-size: 0.78rem; color: var(--text-muted); margin-top: 0.1rem; }
  .tl-status {
    font-size: 0.7rem; padding: 0.2rem 0.7rem;
    text-transform: uppercase; letter-spacing: 0.05em;
  }
  .tl-status.ag { background: rgba(201,168,76,0.12); color: var(--gold); }
  .tl-status.ok { background: rgba(39,174,96,0.12); color: #27ae60; }
  .tl-actions { display: flex; gap: 0.4rem; }
  .tl-btn {
    padding: 0.3rem 0.7rem; font-size: 0.72rem;
    background: none; border: 1px solid rgba(201,168,76,0.25);
    color: var(--gold); cursor: pointer; font-family: 'DM Sans', sans-serif;
    transition: all 0.2s;
  }
  .tl-btn:hover { background: var(--gold); color: var(--black); }
  .tl-btn.del { border-color: rgba(192,57,43,0.3); color: #c0392b; }
  .tl-btn.del:hover { background: #c0392b; color: white; }

  /* agenda completa */
  .filtro-bar {
    display: flex; align-items: center; gap: 0.8rem;
    margin-bottom: 1.5rem; flex-wrap: wrap;
    background: #1a1a1a; border: 1px solid rgba(201,168,76,0.12);
    padding: 1rem 1.2rem;
  }
  .filtro-bar label { font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.1em; }
  .filtro-bar input[type="date"] {
    padding: 0.45rem 0.8rem; background: #2e2e2e;
    border: 1px solid rgba(201,168,76,0.2); color: var(--cream);
    font-family: 'DM Sans', sans-serif; font-size: 0.88rem; outline: none;
    transition: border-color 0.2s;
  }
  .filtro-bar input[type="date"]:focus { border-color: var(--gold); }
  .btn-filtro {
    padding: 0.45rem 1.1rem; background: var(--gold); color: var(--black);
    border: none; cursor: pointer; font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase;
    transition: background 0.2s;
  }
  .btn-filtro:hover { background: var(--gold-light); }
  .btn-limpar {
    padding: 0.45rem 0.9rem; background: none;
    border: 1px solid rgba(201,168,76,0.2); color: var(--text-muted);
    cursor: pointer; font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem; letter-spacing: 0.1em; text-transform: uppercase; transition: all 0.2s;
  }
  .btn-limpar:hover { border-color: var(--gold); color: var(--cream); }

  .agenda-table { width: 100%; border-collapse: collapse; }
  .agenda-table th {
    text-align: left; padding: 0.8rem 1rem;
    font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase;
    color: var(--gold); border-bottom: 1px solid rgba(201,168,76,0.2); font-weight: 400;
  }
  .agenda-table td {
    padding: 0.9rem 1rem; font-size: 0.86rem;
    border-bottom: 1px solid rgba(245,240,232,0.04); vertical-align: middle;
  }
  .agenda-table tr:hover td { background: rgba(201,168,76,0.03); }
  .status-badge {
    display: inline-block; padding: 0.2rem 0.6rem;
    font-size: 0.68rem; letter-spacing: 0.05em;
    text-transform: uppercase;
  }
  .status-agendado { background: rgba(201,168,76,0.12); color: var(--gold); }
  .status-concluido { background: rgba(39,174,96,0.12); color: #27ae60; }
  .btn-concluir {
    padding: 0.28rem 0.7rem; font-size: 0.72rem;
    background: none; border: 1px solid rgba(201,168,76,0.3);
    color: var(--gold); cursor: pointer; font-family: 'DM Sans', sans-serif;
    transition: all 0.2s;
  }
  .btn-concluir:hover { background: var(--gold); color: var(--black); }
  .btn-excluir {
    padding: 0.28rem 0.7rem; font-size: 0.72rem;
    background: none; border: 1px solid rgba(192,57,43,0.3);
    color: #c0392b; cursor: pointer; font-family: 'DM Sans', sans-serif;
    transition: all 0.2s; margin-left: 0.3rem;
  }
  .btn-excluir:hover { background: #c0392b; color: white; }
  .empty-state {
    text-align: center; padding: 3rem;
    color: var(--text-muted); font-size: 0.88rem;
  }
  .empty-state .empty-icon { font-size: 2.5rem; margin-bottom: 0.8rem; }

  /* barra de progresso do dia */
  .progress-bar-wrap { background: #2e2e2e; height: 4px; border-radius: 2px; margin-top: 0.5rem; }
  .progress-bar-fill { height: 4px; background: var(--gold); border-radius: 2px; transition: width 0.5s; }

  /* mini gráfico semanal */
  .semana-grid {
    display: grid; grid-template-columns: repeat(7,1fr); gap: 0.5rem;
    margin-top: 0.8rem;
  }
  .semana-col { display: flex; flex-direction: column; align-items: center; gap: 0.4rem; }
  .semana-bar-wrap { height: 60px; display: flex; align-items: flex-end; width: 100%; justify-content: center; }
  .semana-bar { width: 70%; background: rgba(201,168,76,0.3); border-radius: 2px 2px 0 0; min-height: 4px; transition: height 0.5s; }
  .semana-bar.hoje-bar { background: var(--gold); }
  .semana-dia { font-size: 0.65rem; color: var(--text-muted); text-transform: uppercase; }
  .semana-num { font-size: 0.78rem; color: var(--cream); font-weight: 500; }

  @media (max-width: 900px) {
    .dash-sidebar { width: 60px; }
    .sidebar-logo, .sidebar-item span, .sidebar-footer { display: none; }
    .sidebar-item { justify-content: center; padding: 0.85rem; }
    .kpi-grid { grid-template-columns: repeat(2,1fr); }
    .dash-content { padding: 1.5rem; }
    .dash-topbar { padding: 1rem 1.5rem; }
  }

  /* toast */
  #toast {
    position: fixed; bottom: 2rem; right: 2rem; z-index: 999;
    background: var(--dark); border: 1px solid var(--gold);
    padding: 1rem 1.5rem; font-size: 0.9rem;
    color: var(--cream); transform: translateX(120%);
    transition: transform 0.3s; max-width: 300px;
  }
  #toast.show { transform: translateX(0); }

  /* scroll behavior */
  html { scroll-behavior: smooth; }

  @media (max-width: 700px) {
    nav { padding: 1rem 1.5rem; }
    .nav-links { display: none; }
    .hero-content { padding: 7rem 1.5rem 3rem; }
    .hero-number { display: none; }
    section { padding: 4rem 1.5rem; }
    #agendar { flex-direction: column; gap: 2rem; }
    .horarios-grid { grid-template-columns: repeat(3,1fr); }
    .painel-header { padding: 1rem 1.5rem; flex-wrap: wrap; gap: 0.8rem; }
    .painel-body { padding: 1.5rem; }
    footer { padding: 1.5rem; }
    .form-row { grid-template-columns: 1fr; }
    .agenda-table { display: block; overflow-x: auto; }
  }
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <a class="nav-logo" href="#home">Navalha & Co.</a>
  <div class="nav-links">
    <a href="#home">Início</a>
    <a href="#servicos">Serviços</a>
    <a href="#agendar">Agendar</a>
  </div>
  <button id="btn-barbeiro-nav" onclick="abrirLogin()">Área do Barbeiro</button>
</nav>

<!-- SITE PRINCIPAL -->
<div id="site-publico">

  <!-- HERO -->
  <section id="home" style="padding:0;">
    <div class="hero-bg"></div>
    <div class="hero-line"></div>
    <div class="hero-content">
      <div class="hero-eyebrow">Desde 2018 · Barbearia Premium</div>
      <h1 class="hero-title">Arte<br>que <em>define</em><br>seu estilo.</h1>
      <p class="hero-subtitle">Cada corte é uma obra. Cada barba, um ritual. Venha viver a experiência de uma barbearia que leva a sério o que faz.</p>
      <a class="hero-cta" href="#agendar">Agendar agora</a>
    </div>
    <div class="hero-number">✂</div>
  </section>

  <!-- SERVIÇOS -->
  <section id="servicos">
    <div class="section-label">O que oferecemos</div>
    <h2 class="section-title">Nossos serviços</h2>
    <p style="color:var(--text-muted);max-width:480px;line-height:1.7;font-size:0.95rem;">
      Cada serviço é realizado com precisão cirúrgica e produtos premium. Você sai transformado.
    </p>
    <div class="services-grid">
      <div class="service-card">
        <div class="service-icon">✂️</div>
        <div class="service-name">Corte Clássico</div>
        <div class="service-desc">Corte tradicional com acabamento impecável na navalha e secagem estilizada.</div>
        <div><span class="service-price">R$ 45</span><span class="service-duration">· 45 min</span></div>
      </div>
      <div class="service-card">
        <div class="service-icon">🪒</div>
        <div class="service-name">Barba Completa</div>
        <div class="service-desc">Modelagem com navalha quente, toalha aquecida e balm hidratante pós-barba.</div>
        <div><span class="service-price">R$ 35</span><span class="service-duration">· 30 min</span></div>
      </div>
      <div class="service-card">
        <div class="service-icon">👑</div>
        <div class="service-name">Combo Premium</div>
        <div class="service-desc">Corte + barba completa com ritual de hidratação e finalização profissional.</div>
        <div><span class="service-price">R$ 75</span><span class="service-duration">· 70 min</span></div>
      </div>
      <div class="service-card">
        <div class="service-icon">💆</div>
        <div class="service-name">Pigmentação</div>
        <div class="service-desc">Cobertura de fios brancos na barba ou cabelo com resultado natural e duradouro.</div>
        <div><span class="service-price">R$ 60</span><span class="service-duration">· 60 min</span></div>
      </div>
    </div>
  </section>

  <!-- AGENDAMENTO -->
  <section id="agendar">
    <div class="agendar-info">
      <div class="section-label">Reserve seu horário</div>
      <h2 class="section-title">Agendar<br>atendimento</h2>
      <p style="color:var(--text-muted);line-height:1.8;font-size:0.92rem;max-width:340px;margin-top:1rem;">
        Escolha o serviço, a data e o horário de sua preferência. Confirmação imediata.
      </p>
      <div class="info-list">
        <div class="info-item">
          <span class="info-icon">📍</span>
          <div><div class="info-label">Endereço</div><div class="info-val">Praça da Jabuticaba<br>Quixabeira, BA</div></div>
        </div>
        <div class="info-item">
          <span class="info-icon">🕐</span>
          <div><div class="info-label">Funcionamento</div><div class="info-val">Seg–Sex: 09h às 19h<br>Sáb: 09h às 17h</div></div>
        </div>
        <div class="info-item">
          <span class="info-icon">📱</span>
          <div><div class="info-label">WhatsApp</div><div class="info-val">(64) 99902-8979</div></div>
        </div>
      </div>
    </div>

    <div class="agendar-form-wrap">
      <div class="form-card">
        <div id="form-agendamento">
          <div class="form-group">
            <label>Seu nome</label>
            <input type="text" id="f-nome" placeholder="João Silva">
          </div>
          <div class="form-row">
            <div class="form-group">
              <label>Telefone</label>
              <input type="tel" id="f-tel" placeholder="(75) 9xxxx-xxxx">
            </div>
            <div class="form-group">
              <label>Serviço</label>
              <select id="f-servico">
                <option value="">Escolha...</option>
                <option value="Corte Clássico">Corte Clássico — R$45</option>
                <option value="Barba Completa">Barba Completa — R$35</option>
                <option value="Combo Premium">Combo Premium — R$75</option>
                <option value="Pigmentação">Pigmentação — R$60</option>
              </select>
            </div>
          </div>
          <div class="form-group">
            <label>Data</label>
            <input type="date" id="f-data" onchange="carregarHorarios()">
          </div>
          <div class="form-group">
            <label>Horário disponível</label>
            <div class="horarios-grid" id="horarios-grid">
              <div style="grid-column:1/-1;color:var(--text-muted);font-size:0.82rem;padding:0.5rem 0;">
                Selecione uma data para ver horários disponíveis.
              </div>
            </div>
          </div>
          <button class="btn-submit" onclick="agendar()">Confirmar agendamento</button>
        </div>
        <div id="form-sucesso" style="display:none;text-align:center;padding:2rem 0;">
          <div style="font-size:2.5rem;margin-bottom:1rem;">✅</div>
          <div style="font-family:'Playfair Display',serif;font-size:1.4rem;margin-bottom:0.5rem;">Agendado!</div>
          <div style="color:var(--text-muted);font-size:0.88rem;margin-bottom:1.5rem;" id="sucesso-detalhe"></div>
          <button class="btn-submit" onclick="resetForm()" style="width:auto;padding:0.8rem 2rem;">Fazer novo agendamento</button>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <div class="footer-logo">Navalha & Co.</div>
    <div>© 2025 · Todos os direitos reservados</div>
    <div style="color:var(--text-muted);font-size:0.75rem;">Quixabeira, BA</div>
  </footer>
</div>

<!-- PAINEL DO BARBEIRO — NOVO DASHBOARD -->
<div id="painel">
  <div class="dash-layout">

    <!-- SIDEBAR -->
    <aside class="dash-sidebar">
      <div class="sidebar-logo">
        Navalha & Co.
        <small>Área do barbeiro</small>
      </div>
      <nav class="sidebar-nav">
        <div class="sidebar-item active" onclick="mudarView('overview', this)">
          <span class="s-icon">🏠</span><span>Visão geral</span>
        </div>
        <div class="sidebar-item" onclick="mudarView('agenda', this)">
          <span class="s-icon">📅</span><span>Agenda completa</span>
        </div>
        <div class="sidebar-item" onclick="mudarView('hoje', this)">
          <span class="s-icon">⚡</span><span>Hoje</span>
        </div>
      </nav>
      <div class="sidebar-footer">
        <button class="btn-sair" onclick="sair()">✕ Sair</button>
      </div>
    </aside>

    <!-- MAIN -->
    <main class="dash-main">
      <div class="dash-topbar">
        <div>
          <div class="dash-topbar-title" id="topbar-titulo">Visão Geral</div>
          <div class="dash-topbar-date" id="topbar-data"></div>
        </div>
        <span class="badge-live">ao vivo</span>
      </div>

      <div class="dash-content">

        <!-- VIEW: OVERVIEW -->
        <div class="dash-view active" id="view-overview">
          <!-- KPIs -->
          <div class="kpi-grid" id="kpi-grid"></div>

          <!-- Gráfico semanal + próximos -->
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:2rem;" id="overview-grid">
            <div style="background:#1a1a1a;border:1px solid rgba(201,168,76,0.12);padding:1.5rem;">
              <div style="font-family:'Playfair Display',serif;font-size:1rem;margin-bottom:1.2rem;">Semana atual</div>
              <div class="semana-grid" id="semana-grid"></div>
            </div>
            <div style="background:#1a1a1a;border:1px solid rgba(201,168,76,0.12);padding:1.5rem;">
              <div style="font-family:'Playfair Display',serif;font-size:1rem;margin-bottom:1rem;">Próximos agendamentos</div>
              <div id="proximos-lista"></div>
            </div>
          </div>
        </div>

        <!-- VIEW: AGENDA COMPLETA -->
        <div class="dash-view" id="view-agenda">
          <div class="filtro-bar">
            <label>Data:</label>
            <input type="date" id="filtro-data" oninput="renderAgenda()">
            <button class="btn-filtro" onclick="renderAgenda()">Filtrar</button>
            <button class="btn-limpar" onclick="limparFiltro()">Todos</button>
          </div>
          <div id="agenda-container"></div>
        </div>

        <!-- VIEW: HOJE -->
        <div class="dash-view" id="view-hoje">
          <div class="timeline-section">
            <div class="section-head">
              <h3 id="hoje-titulo"></h3>
              <span id="hoje-progresso" style="font-size:0.78rem;color:var(--text-muted);"></span>
            </div>
            <div id="progress-bar-wrap" class="progress-bar-wrap">
              <div class="progress-bar-fill" id="progress-fill" style="width:0%"></div>
            </div>
            <div class="timeline" id="timeline-hoje" style="margin-top:1.2rem;"></div>
          </div>
        </div>

      </div>
    </main>
  </div>
</div>

<!-- MODAL LOGIN -->
<div class="overlay" id="overlay-login">
  <div class="modal">
    <button class="modal-close" onclick="fecharLogin()">×</button>
    <div class="modal-title">Área do Barbeiro</div>
    <div class="modal-sub">Digite a senha para acessar o painel.</div>
    <input class="modal-input" type="password" id="senha-input" placeholder="Senha"
      onkeydown="if(event.key==='Enter')entrar()">
    <div class="modal-error" id="login-erro">Senha incorreta. Tente novamente.</div>
    <button class="modal-btn" onclick="entrar()">Entrar</button>
  </div>
</div>

<!-- TOAST -->
<div id="toast"></div>

<script>
// ─── DADOS ─────────────────────────────────────────────
const SENHA = 'navalha2025';
const HORARIOS_BASE = ['09:00','09:30','10:00','10:30','11:00','11:30',
                       '14:00','14:30','15:00','15:30','16:00','16:30',
                       '17:00','17:30','18:00','18:30'];

let agendamentos = JSON.parse(localStorage.getItem('agendamentos') || '[]');
let horarioSelecionado = null;
let logado = false;

function salvar() {
  localStorage.setItem('agendamentos', JSON.stringify(agendamentos));
}

// ─── DATA mínima = hoje ─────────────────────────────────
const hoje = new Date().toISOString().split('T')[0];
document.getElementById('f-data').min = hoje;
document.getElementById('filtro-data').value = hoje;

// ─── HORÁRIOS ──────────────────────────────────────────
function carregarHorarios() {
  const data = document.getElementById('f-data').value;
  const grid = document.getElementById('horarios-grid');
  horarioSelecionado = null;
  if (!data) { grid.innerHTML = '<div style="color:var(--text-muted);font-size:0.82rem;padding:0.5rem 0;">Selecione uma data.</div>'; return; }

  // bloqueia sábado tarde e domingo
  const d = new Date(data + 'T12:00:00');
  const diaSemana = d.getDay();
  if (diaSemana === 0) {
    grid.innerHTML = '<div style="color:var(--text-muted);font-size:0.82rem;padding:0.5rem 0;">Não abrimos aos domingos.</div>';
    return;
  }
  const ocupados = agendamentos
    .filter(a => a.data === data && a.status !== 'cancelado')
    .map(a => a.horario);

  // sábado: apenas até 17h
  const horariosValidos = diaSemana === 6
    ? HORARIOS_BASE.filter(h => h <= '16:30')
    : HORARIOS_BASE;

  grid.innerHTML = horariosValidos.map(h => {
    const ocu = ocupados.includes(h);
    return `<button class="horario-btn${ocu?' ocupado':''}" onclick="${ocu?'':'selecionarHorario(this,\''+h+'\')'}">
      ${h}
    </button>`;
  }).join('');
}

function selecionarHorario(btn, h) {
  document.querySelectorAll('.horario-btn').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
  horarioSelecionado = h;
}

// ─── AGENDAR ───────────────────────────────────────────
function agendar() {
  const nome = document.getElementById('f-nome').value.trim();
  const tel = document.getElementById('f-tel').value.trim();
  const servico = document.getElementById('f-servico').value;
  const data = document.getElementById('f-data').value;

  if (!nome || !tel || !servico || !data || !horarioSelecionado) {
    toast('Preencha todos os campos e escolha um horário.');
    return;
  }

  const novo = {
    id: Date.now().toString(),
    nome, tel, servico, data,
    horario: horarioSelecionado,
    status: 'agendado',
    criadoEm: new Date().toISOString()
  };
  agendamentos.push(novo);
  salvar();

  document.getElementById('form-agendamento').style.display = 'none';
  document.getElementById('form-sucesso').style.display = 'block';
  document.getElementById('sucesso-detalhe').textContent =
    `${servico} · ${formatarData(data)} às ${horarioSelecionado}`;
}

function resetForm() {
  document.getElementById('form-agendamento').style.display = 'block';
  document.getElementById('form-sucesso').style.display = 'none';
  document.getElementById('f-nome').value = '';
  document.getElementById('f-tel').value = '';
  document.getElementById('f-servico').value = '';
  document.getElementById('f-data').value = '';
  document.getElementById('horarios-grid').innerHTML =
    '<div style="color:var(--text-muted);font-size:0.82rem;padding:0.5rem 0;">Selecione uma data para ver horários disponíveis.</div>';
  horarioSelecionado = null;
}

// ─── LOGIN ─────────────────────────────────────────────
function abrirLogin() {
  document.getElementById('overlay-login').classList.add('active');
  setTimeout(() => document.getElementById('senha-input').focus(), 100);
}
function fecharLogin() {
  document.getElementById('overlay-login').classList.remove('active');
  document.getElementById('senha-input').value = '';
  document.getElementById('login-erro').style.display = 'none';
}
function entrar() {
  const s = document.getElementById('senha-input').value;
  if (s === SENHA) {
    logado = true;
    fecharLogin();
    abrirPainel();
  } else {
    document.getElementById('login-erro').style.display = 'block';
    document.getElementById('senha-input').value = '';
    document.getElementById('senha-input').focus();
  }
}
function sair() {
  logado = false;
  document.getElementById('painel').classList.remove('active');
  document.getElementById('site-publico').style.display = 'block';
}

// ─── PAINEL ────────────────────────────────────────────
function abrirPainel() {
  document.getElementById('site-publico').style.display = 'none';
  document.getElementById('painel').classList.add('active');
  // data topbar
  const agora = new Date();
  const dias = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado'];
  const meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'];
  document.getElementById('topbar-data').textContent =
    `${dias[agora.getDay()]}, ${agora.getDate()} de ${meses[agora.getMonth()]}`;
  document.getElementById('filtro-data').value = hoje;
  window.scrollTo(0,0);
  renderOverview();
  renderAgenda();
  renderHoje();
}

function mudarView(view, el) {
  document.querySelectorAll('.sidebar-item').forEach(i => i.classList.remove('active'));
  el.classList.add('active');
  document.querySelectorAll('.dash-view').forEach(v => v.classList.remove('active'));
  document.getElementById('view-' + view).classList.add('active');
  const titulos = { overview: 'Visão Geral', agenda: 'Agenda Completa', hoje: 'Hoje' };
  document.getElementById('topbar-titulo').textContent = titulos[view];
  if (view === 'overview') renderOverview();
  if (view === 'agenda') renderAgenda();
  if (view === 'hoje') renderHoje();
}

function recarregar() { agendamentos = JSON.parse(localStorage.getItem('agendamentos') || '[]'); }

// ── OVERVIEW ──
function renderOverview() {
  recarregar();
  const total = agendamentos.length;
  const hojeAg = agendamentos.filter(a => a.data === hoje && a.status !== 'cancelado').length;
  const concluidos = agendamentos.filter(a => a.status === 'concluido').length;
  const pendentes = agendamentos.filter(a => a.status === 'agendado').length;

  // receita estimada (preços fixos)
  const precos = { 'Corte Clássico': 45, 'Barba Completa': 35, 'Combo Premium': 75, 'Pigmentação': 60 };
  const receita = agendamentos.filter(a => a.status === 'concluido')
    .reduce((s, a) => s + (precos[a.servico] || 0), 0);

  document.getElementById('kpi-grid').innerHTML = `
    <div class="kpi-card"><div class="kpi-icon">⚡</div>
      <div class="kpi-val">${hojeAg}</div>
      <div class="kpi-label">Hoje</div>
      <div class="kpi-change neutral">agendamentos do dia</div></div>
    <div class="kpi-card"><div class="kpi-icon">🕐</div>
      <div class="kpi-val">${pendentes}</div>
      <div class="kpi-label">Pendentes</div>
      <div class="kpi-change neutral">aguardando atendimento</div></div>
    <div class="kpi-card"><div class="kpi-icon">✅</div>
      <div class="kpi-val">${concluidos}</div>
      <div class="kpi-label">Concluídos</div>
      <div class="kpi-change up">↑ atendimentos finalizados</div></div>
    <div class="kpi-card"><div class="kpi-icon">💰</div>
      <div class="kpi-val">R$<span>${receita}</span></div>
      <div class="kpi-label">Receita</div>
      <div class="kpi-change up">serviços concluídos</div></div>
  `;

  // gráfico semanal
  const diaSemana = new Date().getDay();
  const nomes = ['Dom','Seg','Ter','Qua','Qui','Sex','Sáb'];
  const semana = [];
  for (let i = 0; i < 7; i++) {
    const d = new Date();
    d.setDate(d.getDate() - diaSemana + i);
    const ds = d.toISOString().split('T')[0];
    const count = agendamentos.filter(a => a.data === ds && a.status !== 'cancelado').length;
    semana.push({ nome: nomes[i], count, isHoje: i === diaSemana, ds });
  }
  const maxC = Math.max(...semana.map(s => s.count), 1);
  document.getElementById('semana-grid').innerHTML = semana.map(s => `
    <div class="semana-col">
      <div class="semana-bar-wrap">
        <div class="semana-bar${s.isHoje?' hoje-bar':''}" style="height:${Math.round((s.count/maxC)*56)+4}px"></div>
      </div>
      <div class="semana-num">${s.count}</div>
      <div class="semana-dia">${s.nome}</div>
    </div>
  `).join('');

  // próximos
  const agora2 = new Date();
  const proximos = agendamentos
    .filter(a => a.status === 'agendado' && (a.data > hoje || (a.data === hoje && a.horario >= agora2.toTimeString().slice(0,5))))
    .sort((a,b) => a.data !== b.data ? a.data.localeCompare(b.data) : a.horario.localeCompare(b.horario))
    .slice(0, 5);
  document.getElementById('proximos-lista').innerHTML = proximos.length === 0
    ? '<div style="color:var(--text-muted);font-size:0.82rem;">Nenhum agendamento futuro.</div>'
    : proximos.map(a => `
      <div style="display:flex;align-items:center;gap:0.8rem;padding:0.7rem 0;border-bottom:1px solid rgba(245,240,232,0.05);">
        <div style="font-family:\'Playfair Display\',serif;color:var(--gold);font-size:0.9rem;min-width:42px;">${a.horario}</div>
        <div>
          <div style="font-size:0.84rem;font-weight:500;">${a.nome}</div>
          <div style="font-size:0.72rem;color:var(--text-muted);">${a.servico} · ${formatarData(a.data)}</div>
        </div>
      </div>`).join('');
}

// ── AGENDA COMPLETA ──
function renderAgenda() {
  recarregar();
  const filtroData = document.getElementById('filtro-data').value;
  let lista = [...agendamentos].sort((a,b) => {
    if (a.data !== b.data) return a.data.localeCompare(b.data);
    return a.horario.localeCompare(b.horario);
  });
  if (filtroData) lista = lista.filter(a => a.data === filtroData);

  const c = document.getElementById('agenda-container');
  if (lista.length === 0) {
    c.innerHTML = `<div class="empty-state"><div class="empty-icon">📅</div>
      <div>${filtroData?'Nenhum agendamento nesta data.':'Nenhum agendamento ainda.'}</div></div>`;
    return;
  }
  c.innerHTML = `<table class="agenda-table">
    <thead><tr>
      <th>Horário</th><th>Data</th><th>Cliente</th>
      <th>Serviço</th><th>Telefone</th><th>Status</th><th>Ações</th>
    </tr></thead>
    <tbody>${lista.map(a=>`<tr>
      <td><strong>${a.horario}</strong></td>
      <td>${formatarData(a.data)}</td>
      <td>${a.nome}</td><td>${a.servico}</td><td>${a.tel}</td>
      <td><span class="status-badge ${a.status==='concluido'?'status-concluido':'status-agendado'}">
        ${a.status==='concluido'?'Concluído':'Agendado'}</span></td>
      <td>${a.status==='agendado'?`<button class="btn-concluir" onclick="concluir('${a.id}')">✓</button>`:''}
        <button class="btn-excluir" onclick="excluir('${a.id}')">✕</button></td>
    </tr>`).join('')}</tbody></table>`;
}

// ── HOJE ──
function renderHoje() {
  recarregar();
  const lista = agendamentos
    .filter(a => a.data === hoje && a.status !== 'cancelado')
    .sort((a,b) => a.horario.localeCompare(b.horario));

  const d = new Date();
  const meses2 = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];
  document.getElementById('hoje-titulo').textContent = `${d.getDate()} de ${meses2[d.getMonth()]}`;

  const total = lista.length;
  const feitos = lista.filter(a => a.status==='concluido').length;
  const pct = total > 0 ? Math.round((feitos/total)*100) : 0;
  document.getElementById('hoje-progresso').textContent = `${feitos}/${total} concluídos`;
  document.getElementById('progress-fill').style.width = pct + '%';

  const tl = document.getElementById('timeline-hoje');
  if (lista.length === 0) {
    tl.innerHTML = '<div class="empty-state"><div class="empty-icon">☕</div><div>Sem agendamentos hoje.</div></div>';
    return;
  }
  tl.innerHTML = lista.map(a => `
    <div class="timeline-item">
      <div class="tl-hora">${a.horario}</div>
      <div class="tl-divider"></div>
      <div class="tl-info">
        <div class="tl-nome">${a.nome}</div>
        <div class="tl-serv">${a.servico} · ${a.tel}</div>
      </div>
      <span class="tl-status ${a.status==='concluido'?'ok':'ag'}">${a.status==='concluido'?'✓ Feito':'Aguardando'}</span>
      <div class="tl-actions">
        ${a.status==='agendado'?`<button class="tl-btn" onclick="concluirHoje('${a.id}')">✓</button>`:''}
        <button class="tl-btn del" onclick="excluirHoje('${a.id}')">✕</button>
      </div>
    </div>`).join('');
}

function concluirHoje(id) {
  const i = agendamentos.findIndex(a => a.id===id);
  if (i!==-1){ agendamentos[i].status='concluido'; salvar(); renderHoje(); renderOverview(); }
}
function excluirHoje(id) {
  if (!confirm('Excluir agendamento?')) return;
  agendamentos = agendamentos.filter(a => a.id!==id);
  salvar(); renderHoje(); renderOverview();
}

function renderPainel() { renderAgenda(); }

function concluir(id) {
  const i = agendamentos.findIndex(a => a.id === id);
  if (i !== -1) { agendamentos[i].status = 'concluido'; salvar(); renderAgenda(); renderOverview(); }
}
function excluir(id) {
  if (!confirm('Excluir este agendamento?')) return;
  agendamentos = agendamentos.filter(a => a.id !== id);
  salvar(); renderAgenda(); renderOverview();
  toast('Agendamento removido.');
}
function limparFiltro() {
  document.getElementById('filtro-data').value = '';
  renderAgenda();
}

// ─── UTILS ─────────────────────────────────────────────
function formatarData(d) {
  if (!d) return '';
  const [y,m,dd] = d.split('-');
  return `${dd}/${m}/${y}`;
}
function toast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg; t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 3000);
}

// fechar overlay clicando fora
document.getElementById('overlay-login').addEventListener('click', function(e) {
  if (e.target === this) fecharLogin();
});
</script>
</body>
</html>
