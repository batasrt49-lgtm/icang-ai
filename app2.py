<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NOVA AI</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0A0A0B;--bg2:#111113;--bg3:#18181B;--bg4:#222228;
  --fg:#FAFAFA;--fg2:#A1A1AA;--fg3:#52525B;
  --accent:#7C3AED;--accent2:#9B59F5;--accent-glow:rgba(124,58,237,0.15);
  --border:rgba(255,255,255,0.08);--border2:rgba(255,255,255,0.12);
  --r:10px;--r-lg:16px;--r-xl:20px;
  --sidebar:260px;
}
html,body{height:100%;background:var(--bg);color:var(--fg);font-family:'Inter',sans-serif;font-size:14px;line-height:1.6;overflow:hidden}
button{cursor:pointer;font-family:inherit;border:none;outline:none}
input,textarea{font-family:inherit;outline:none;border:none}
a{color:inherit;text-decoration:none}
::-webkit-scrollbar{width:4px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--bg4);border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:var(--fg3)}

/* AUTH */
#auth-screen{
  position:fixed;inset:0;background:var(--bg);
  display:flex;align-items:center;justify-content:center;z-index:100;
}
.auth-card{
  width:380px;background:var(--bg2);border:1px solid var(--border2);
  border-radius:var(--r-xl);padding:36px 32px;
}
.auth-logo{display:flex;align-items:center;gap:10px;margin-bottom:28px}
.auth-logo-icon{
  width:40px;height:40px;background:var(--accent);border-radius:10px;
  display:flex;align-items:center;justify-content:center;font-size:20px;color:#fff;
}
.auth-logo-text{font-size:20px;font-weight:700;letter-spacing:-.02em}
.auth-logo-sub{font-size:12px;color:var(--fg3);margin-top:1px}
.auth-title{font-size:22px;font-weight:700;letter-spacing:-.02em;margin-bottom:6px}
.auth-sub{font-size:13px;color:var(--fg2);margin-bottom:28px}
.auth-tabs{display:flex;background:var(--bg3);border-radius:var(--r);padding:3px;margin-bottom:24px}
.auth-tab{
  flex:1;padding:7px;text-align:center;font-size:13px;font-weight:500;
  border-radius:8px;color:var(--fg3);transition:.2s;cursor:pointer;
}
.auth-tab.active{background:var(--bg4);color:var(--fg)}
.field{margin-bottom:14px}
.field label{display:block;font-size:12px;font-weight:500;color:var(--fg2);margin-bottom:6px;letter-spacing:.04em;text-transform:uppercase}
.field input{
  width:100%;background:var(--bg3);border:1px solid var(--border2);
  border-radius:var(--r);padding:10px 14px;color:var(--fg);font-size:14px;transition:.2s;
}
.field input:focus{border-color:var(--accent);background:var(--bg4)}
.field input::placeholder{color:var(--fg3)}
.btn-primary{
  width:100%;padding:11px;background:var(--accent);color:#fff;
  border-radius:var(--r);font-size:14px;font-weight:600;transition:.2s;margin-top:8px;
}
.btn-primary:hover{background:var(--accent2);transform:translateY(-1px)}
.btn-primary:active{transform:translateY(0)}
.auth-error{
  background:rgba(239,68,68,.1);border:1px solid rgba(239,68,68,.25);
  border-radius:var(--r);padding:10px 14px;font-size:13px;color:#F87171;
  margin-bottom:14px;display:none;
}
.auth-demo{
  margin-top:20px;padding-top:20px;border-top:1px solid var(--border);
  text-align:center;font-size:12px;color:var(--fg3);
}
.auth-demo span{color:var(--accent2);cursor:pointer;font-weight:500}
.auth-demo span:hover{text-decoration:underline}

/* MAIN APP */
#app{display:flex;height:100vh;position:relative}
#app.hidden{display:none}

/* SIDEBAR */
.sidebar{
  width:var(--sidebar);background:var(--bg2);border-right:1px solid var(--border);
  display:flex;flex-direction:column;flex-shrink:0;
}
.sidebar-header{
  padding:16px;border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;
}
.logo{display:flex;align-items:center;gap:8px}
.logo-icon{
  width:30px;height:30px;background:var(--accent);border-radius:8px;
  display:flex;align-items:center;justify-content:center;font-size:15px;color:#fff;
}
.logo-text{font-size:16px;font-weight:700;letter-spacing:-.02em}
.btn-new{
  width:30px;height:30px;background:var(--bg4);border:1px solid var(--border2);
  border-radius:8px;display:flex;align-items:center;justify-content:center;
  color:var(--fg2);transition:.2s;font-size:16px;
}
.btn-new:hover{background:var(--accent);color:#fff;border-color:var(--accent)}
.sidebar-search{padding:10px 12px;border-bottom:1px solid var(--border)}
.search-wrap{
  display:flex;align-items:center;gap:8px;background:var(--bg3);
  border:1px solid var(--border);border-radius:var(--r);padding:6px 10px;
}
.search-wrap i{color:var(--fg3);font-size:14px}
.search-wrap input{background:transparent;color:var(--fg);font-size:13px;flex:1;min-width:0}
.search-wrap input::placeholder{color:var(--fg3)}
.sidebar-section{
  padding:10px 12px 4px;font-size:11px;font-weight:600;
  letter-spacing:.08em;text-transform:uppercase;color:var(--fg3);
}
.sidebar-list{flex:1;overflow-y:auto;padding:0 8px 8px}
.chat-item{
  padding:10px;border-radius:var(--r);cursor:pointer;margin-bottom:2px;
  transition:.15s;display:flex;align-items:flex-start;gap:8px;border:1px solid transparent;
}
.chat-item:hover{background:var(--bg3);border-color:var(--border)}
.chat-item.active{background:var(--accent-glow);border-color:rgba(124,58,237,.3)}
.chat-item-icon{
  width:28px;height:28px;background:var(--bg4);border-radius:7px;
  display:flex;align-items:center;justify-content:center;font-size:13px;color:var(--fg3);flex-shrink:0;margin-top:1px;
}
.chat-item.active .chat-item-icon{background:var(--accent);color:#fff}
.chat-item-info{min-width:0;flex:1}
.chat-item-title{
  font-size:13px;font-weight:500;color:var(--fg);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-bottom:2px;
}
.chat-item.active .chat-item-title{color:#C4B5FD}
.chat-item-meta{font-size:11px;color:var(--fg3)}
.chat-item-actions{display:none;gap:2px;flex-shrink:0}
.chat-item:hover .chat-item-actions{display:flex}
.chat-item-btn{
  width:22px;height:22px;border-radius:5px;background:transparent;
  display:flex;align-items:center;justify-content:center;font-size:13px;color:var(--fg3);transition:.15s;
}
.chat-item-btn:hover{background:var(--bg4);color:var(--fg)}
.chat-item-btn.del:hover{color:#F87171;background:rgba(239,68,68,.1)}
.sidebar-bottom{padding:12px;border-top:1px solid var(--border)}
.user-card{
  display:flex;align-items:center;gap:10px;padding:8px 10px;
  border-radius:var(--r);cursor:pointer;transition:.15s;border:1px solid transparent;
}
.user-card:hover{background:var(--bg3);border-color:var(--border)}
.avatar{
  width:32px;height:32px;border-radius:50%;background:var(--accent);
  display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;color:#fff;flex-shrink:0;
}
.user-info{flex:1;min-width:0}
.user-name{font-size:13px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.user-plan{font-size:11px;color:var(--fg3)}
.user-menu-icon{color:var(--fg3);font-size:16px}

/* MAIN CHAT */
.main{flex:1;display:flex;flex-direction:column;min-width:0;overflow:hidden}
.chat-header{
  padding:14px 20px;border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;
  background:var(--bg2);flex-shrink:0;
}
.chat-header-info{display:flex;align-items:center;gap:10px}
.model-badge{
  display:flex;align-items:center;gap:6px;padding:5px 12px;
  background:var(--bg4);border:1px solid var(--border2);border-radius:20px;
  font-size:12px;font-weight:500;color:var(--fg2);cursor:pointer;transition:.15s;
}
.model-badge:hover{border-color:var(--accent);color:var(--accent2)}
.model-dot{width:6px;height:6px;border-radius:50%;background:#22C55E}
.chat-title-wrap{flex:1;min-width:0;margin:0 12px}
.chat-title{font-size:14px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.header-actions{display:flex;gap:6px}
.icon-btn{
  width:32px;height:32px;background:transparent;border:1px solid var(--border);
  border-radius:var(--r);display:flex;align-items:center;justify-content:center;
  color:var(--fg3);font-size:16px;transition:.15s;
}
.icon-btn:hover{background:var(--bg3);border-color:var(--border2);color:var(--fg)}

/* MESSAGES */
.messages{flex:1;overflow-y:auto;padding:20px}
.messages-inner{max-width:760px;margin:0 auto}
.empty-state{
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  height:100%;text-align:center;padding:40px;
}
.empty-icon{
  width:64px;height:64px;background:var(--accent-glow);border:1px solid rgba(124,58,237,.25);
  border-radius:16px;display:flex;align-items:center;justify-content:center;
  font-size:28px;color:var(--accent2);margin-bottom:20px;
}
.empty-title{font-size:22px;font-weight:700;letter-spacing:-.02em;margin-bottom:8px}
.empty-sub{font-size:14px;color:var(--fg2);max-width:380px;line-height:1.7;margin-bottom:28px}
.suggestion-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;width:100%;max-width:480px}
.suggestion{
  padding:12px 14px;background:var(--bg3);border:1px solid var(--border2);
  border-radius:var(--r);cursor:pointer;text-align:left;
  font-size:13px;color:var(--fg2);line-height:1.5;transition:.2s;
}
.suggestion:hover{background:var(--bg4);border-color:var(--accent);color:var(--fg)}
.suggestion strong{display:block;font-size:12px;font-weight:600;color:var(--fg);margin-bottom:3px}
.msg-wrap{display:flex;gap:10px;margin-bottom:24px;align-items:flex-start}
.msg-wrap.user{flex-direction:row-reverse}
.msg-avatar{
  width:30px;height:30px;border-radius:50%;display:flex;align-items:center;
  justify-content:center;font-size:14px;flex-shrink:0;margin-top:2px;
}
.msg-avatar.ai{background:var(--accent);color:#fff}
.msg-avatar.user-av{background:var(--bg4);border:1px solid var(--border2);color:var(--fg2);font-size:13px;font-weight:600}
.msg-content{max-width:75%;min-width:0}
.msg-wrap.user .msg-content{align-items:flex-end;display:flex;flex-direction:column}
.bubble{padding:11px 15px;border-radius:var(--r-lg);font-size:14px;line-height:1.7;word-break:break-word}
.bubble.ai{
  background:var(--bg3);border:1px solid var(--border);
  border-radius:4px var(--r-lg) var(--r-lg) var(--r-lg);color:var(--fg);
}
.bubble.user-b{
  background:var(--accent);color:#fff;
  border-radius:var(--r-lg) var(--r-lg) 4px var(--r-lg);
}
.bubble code{
  font-family:'JetBrains Mono',monospace;font-size:12px;
  background:rgba(255,255,255,.08);padding:2px 6px;border-radius:4px;
}
.bubble pre{
  background:var(--bg);border:1px solid var(--border2);border-radius:var(--r);
  padding:12px;margin:10px 0;overflow-x:auto;
  font-family:'JetBrains Mono',monospace;font-size:12.5px;line-height:1.6;
}
.bubble pre code{background:transparent;padding:0}
.bubble p{margin-bottom:10px}
.bubble p:last-child{margin-bottom:0}
.bubble h1,.bubble h2,.bubble h3{font-weight:600;margin:14px 0 8px;line-height:1.4}
.bubble h1{font-size:18px}.bubble h2{font-size:16px}.bubble h3{font-size:14px}
.bubble ul,.bubble ol{padding-left:20px;margin-bottom:10px}
.bubble li{margin-bottom:4px}
.bubble blockquote{
  border-left:3px solid var(--accent);padding-left:12px;
  color:var(--fg2);margin:10px 0;font-style:italic;
}
.bubble strong{font-weight:600;color:var(--fg)}
.bubble em{font-style:italic;color:var(--fg2)}
.bubble table{width:100%;border-collapse:collapse;margin:10px 0;font-size:13px}
.bubble td,.bubble th{border:1px solid var(--border2);padding:7px 10px}
.bubble th{background:var(--bg4);font-weight:600}
.msg-meta{display:flex;align-items:center;gap:8px;margin-top:5px;padding:0 2px}
.msg-time{font-size:11px;color:var(--fg3)}
.msg-actions{display:flex;gap:2px;opacity:0;transition:.15s}
.msg-wrap:hover .msg-actions{opacity:1}
.msg-action-btn{
  padding:3px 6px;border-radius:5px;background:transparent;
  color:var(--fg3);font-size:12px;transition:.15s;display:flex;align-items:center;gap:4px;
}
.msg-action-btn:hover{background:var(--bg4);color:var(--fg)}
.typing{display:flex;align-items:center;gap:5px;padding:11px 15px}
.typing span{width:7px;height:7px;background:var(--fg3);border-radius:50%;animation:bounce .9s ease-in-out infinite}
.typing span:nth-child(2){animation-delay:.15s}
.typing span:nth-child(3){animation-delay:.3s}
@keyframes bounce{0%,80%,100%{transform:translateY(0)}40%{transform:translateY(-6px)}}

/* INPUT */
.input-area{
  padding:14px 20px 16px;border-top:1px solid var(--border);
  background:var(--bg2);flex-shrink:0;
}
.input-wrap{
  max-width:760px;margin:0 auto;background:var(--bg3);
  border:1px solid var(--border2);border-radius:var(--r-lg);padding:4px;transition:.2s;
}
.input-wrap:focus-within{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-glow)}
.input-inner{display:flex;align-items:flex-end;gap:8px;padding:8px 8px 4px}
#chat-input{
  flex:1;background:transparent;color:var(--fg);font-size:14px;
  resize:none;max-height:140px;line-height:1.6;padding:2px 4px;min-height:24px;
}
#chat-input::placeholder{color:var(--fg3)}
.input-actions{display:flex;align-items:center;gap:4px;padding:0 8px 8px;justify-content:space-between}
.input-hints{display:flex;gap:4px;flex-wrap:wrap}
.hint-chip{
  display:flex;align-items:center;gap:5px;padding:4px 10px;
  background:var(--bg4);border:1px solid var(--border);border-radius:20px;
  font-size:12px;color:var(--fg3);cursor:pointer;transition:.15s;
}
.hint-chip:hover{border-color:var(--border2);color:var(--fg)}
.send-btn{
  width:34px;height:34px;background:var(--accent);border-radius:var(--r);
  display:flex;align-items:center;justify-content:center;font-size:16px;color:#fff;transition:.2s;flex-shrink:0;
}
.send-btn:hover{background:var(--accent2);transform:scale(1.05)}
.send-btn:disabled{background:var(--bg4);color:var(--fg3);transform:none;cursor:not-allowed}
.input-footer{text-align:center;font-size:11px;color:var(--fg3);padding:8px 0 0}

/* MODEL PICKER */
.model-picker{
  position:fixed;top:60px;left:calc(var(--sidebar) + 20px);
  background:var(--bg2);border:1px solid var(--border2);border-radius:var(--r-lg);
  padding:6px;width:280px;box-shadow:0 16px 48px rgba(0,0,0,.4);z-index:50;display:none;
}
.model-picker.open{display:block}
.model-item{
  padding:10px 12px;border-radius:var(--r);cursor:pointer;transition:.15s;
  display:flex;align-items:center;gap:10px;
}
.model-item:hover{background:var(--bg3)}
.model-item.active{background:var(--accent-glow)}
.model-item-info{flex:1}
.model-item-name{font-size:13px;font-weight:500}
.model-item.active .model-item-name{color:var(--accent2)}
.model-item-desc{font-size:11px;color:var(--fg3);margin-top:1px}
.model-check{color:var(--accent2);font-size:16px;opacity:0}
.model-item.active .model-check{opacity:1}
.model-item-badge{
  font-size:10px;font-weight:600;padding:2px 7px;border-radius:4px;
  background:rgba(124,58,237,.15);color:var(--accent2);letter-spacing:.04em;
}

/* USER DROPDOWN */
.user-dropdown{
  position:absolute;bottom:70px;left:12px;width:240px;
  background:var(--bg2);border:1px solid var(--border2);border-radius:var(--r-lg);
  padding:6px;box-shadow:0 16px 40px rgba(0,0,0,.4);z-index:50;display:none;
}
.user-dropdown.open{display:block}
.dropdown-item{
  padding:9px 12px;border-radius:var(--r);cursor:pointer;transition:.15s;
  display:flex;align-items:center;gap:10px;font-size:13px;color:var(--fg2);
}
.dropdown-item:hover{background:var(--bg3);color:var(--fg)}
.dropdown-item.danger:hover{background:rgba(239,68,68,.1);color:#F87171}
.dropdown-item i{font-size:16px}
.dropdown-divider{height:1px;background:var(--border);margin:4px 0}
.dropdown-header{padding:8px 12px;font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--fg3)}

/* TOAST */
.toast{
  position:fixed;bottom:20px;right:20px;padding:10px 16px;
  background:var(--bg2);border:1px solid var(--border2);border-radius:var(--r);
  font-size:13px;color:var(--fg);box-shadow:0 8px 24px rgba(0,0,0,.3);
  transform:translateY(10px);opacity:0;transition:.3s;pointer-events:none;z-index:200;
  display:flex;align-items:center;gap:8px;
}
.toast.show{transform:translateY(0);opacity:1}
.toast-icon{font-size:16px}
</style>
</head>
<body>

<!-- AUTH SCREEN -->
<div id="auth-screen">
  <div class="auth-card">
    <div class="auth-logo">
      <div class="auth-logo-icon"><i class="ti ti-sparkles"></i></div>
      <div>
        <div class="auth-logo-text">NOVA AI</div>
        <div class="auth-logo-sub">Powered by Claude</div>
      </div>
    </div>
    <div class="auth-title" id="auth-title">Selamat datang kembali</div>
    <div class="auth-sub" id="auth-sub">Masuk untuk melanjutkan percakapanmu</div>
    <div class="auth-tabs">
      <div class="auth-tab active" id="tab-login" onclick="switchTab('login')">Masuk</div>
      <div class="auth-tab" id="tab-register" onclick="switchTab('register')">Daftar</div>
    </div>
    <div class="auth-error" id="auth-error"></div>
    <div class="field">
      <label>Email</label>
      <input type="email" id="auth-email" placeholder="kamu@email.com">
    </div>
    <div class="field" id="field-name" style="display:none">
      <label>Nama</label>
      <input type="text" id="auth-name" placeholder="Nama kamu">
    </div>
    <div class="field">
      <label>Password</label>
      <input type="password" id="auth-pass" placeholder="••••••••" onkeydown="if(event.key==='Enter')doAuth()">
    </div>
    <button class="btn-primary" onclick="doAuth()" id="auth-btn">Masuk</button>
    <div class="auth-demo">
      Mau coba dulu? <span onclick="demoLogin()">Login sebagai Demo</span>
    </div>
  </div>
</div>

<!-- MAIN APP -->
<div id="app" class="hidden">
  <!-- SIDEBAR -->
  <div class="sidebar">
    <div class="sidebar-header">
      <div class="logo">
        <div class="logo-icon"><i class="ti ti-sparkles"></i></div>
        <div class="logo-text">NOVA AI</div>
      </div>
      <button class="btn-new" onclick="newChat()" title="Chat baru">
        <i class="ti ti-edit"></i>
      </button>
    </div>
    <div class="sidebar-search">
      <div class="search-wrap">
        <i class="ti ti-search"></i>
        <input type="text" placeholder="Cari percakapan..." id="search-input" oninput="filterChats()">
      </div>
    </div>
    <div class="sidebar-list" id="chat-list"></div>
    <div class="sidebar-bottom">
      <div class="user-card" onclick="toggleUserMenu()">
        <div class="avatar" id="user-avatar"></div>
        <div class="user-info">
          <div class="user-name" id="user-name-display"></div>
          <div class="user-plan">Free Plan · Claude Powered</div>
        </div>
        <i class="ti ti-dots-vertical user-menu-icon"></i>
      </div>
      <div class="user-dropdown" id="user-dropdown">
        <div class="dropdown-header">Akun</div>
        <div class="dropdown-item"><i class="ti ti-user"></i>Profil</div>
        <div class="dropdown-item"><i class="ti ti-settings"></i>Pengaturan</div>
        <div class="dropdown-divider"></div>
        <div class="dropdown-item" onclick="exportChats()"><i class="ti ti-download"></i>Export Percakapan</div>
        <div class="dropdown-item" onclick="clearAllChats()"><i class="ti ti-trash"></i>Hapus Semua</div>
        <div class="dropdown-divider"></div>
        <div class="dropdown-item danger" onclick="logout()"><i class="ti ti-logout"></i>Keluar</div>
      </div>
    </div>
  </div>

  <!-- MAIN CHAT -->
  <div class="main">
    <div class="chat-header">
      <div class="model-badge" onclick="toggleModelPicker()">
        <div class="model-dot"></div>
        <span id="model-label">claude-sonnet-4-6</span>
        <i class="ti ti-chevron-down" style="font-size:12px"></i>
      </div>
      <div class="chat-title-wrap">
        <div class="chat-title" id="chat-header-title">Chat Baru</div>
      </div>
      <div class="header-actions">
        <button class="icon-btn" onclick="shareChat()" title="Bagikan"><i class="ti ti-share"></i></button>
        <button class="icon-btn" onclick="clearCurrentChat()" title="Hapus pesan"><i class="ti ti-trash"></i></button>
      </div>
    </div>

    <div class="messages" id="messages">
      <div class="messages-inner" id="messages-inner">
        <div class="empty-state" id="empty-state">
          <div class="empty-icon"><i class="ti ti-sparkles"></i></div>
          <div class="empty-title">Halo! Saya NOVA.</div>
          <div class="empty-sub">AI assistant yang siap membantu kamu kapan saja. Tanya apa saja — dari kode, cerita, hingga analisis data.</div>
          <div class="suggestion-grid">
            <button class="suggestion" onclick="useSuggestion('Jelaskan konsep machine learning dengan sederhana')"><strong>📚 Belajar</strong>Jelaskan machine learning dengan sederhana</button>
            <button class="suggestion" onclick="useSuggestion('Buat cerita pendek tentang petualangan di luar angkasa')"><strong>✍️ Kreatif</strong>Tulis cerita petualangan luar angkasa</button>
            <button class="suggestion" onclick="useSuggestion('Bantu saya debug kode Python ini')"><strong>💻 Coding</strong>Debug kode Python saya</button>
            <button class="suggestion" onclick="useSuggestion('Buat rencana belajar bahasa Inggris selama 30 hari')"><strong>📋 Rencana</strong>Rencana belajar bahasa Inggris 30 hari</button>
          </div>
        </div>
      </div>
    </div>

    <div class="input-area">
      <div class="input-wrap">
        <div class="input-inner">
          <textarea id="chat-input" placeholder="Ketik pesan..." rows="1"
            onkeydown="handleKey(event)" oninput="autoResize(this)"></textarea>
          <button class="send-btn" id="send-btn" onclick="sendMessage()" disabled>
            <i class="ti ti-send"></i>
          </button>
        </div>
        <div class="input-actions">
          <div class="input-hints">
            <div class="hint-chip"><i class="ti ti-code" style="font-size:13px"></i>Kode</div>
            <div class="hint-chip"><i class="ti ti-pencil" style="font-size:13px"></i>Tulis</div>
            <div class="hint-chip"><i class="ti ti-math" style="font-size:13px"></i>Hitung</div>
            <div class="hint-chip"><i class="ti ti-language" style="font-size:13px"></i>Terjemah</div>
          </div>
          <span style="font-size:11px;color:var(--fg3)">Enter kirim · Shift+Enter baris baru</span>
        </div>
      </div>
      <div class="input-footer">NOVA AI · Powered by Claude · Dapat membuat kesalahan</div>
    </div>
  </div>

  <!-- MODEL PICKER -->
  <div class="model-picker" id="model-picker">
    <div class="model-item active" onclick="selectModel('claude-sonnet-4-6','Claude Sonnet 4.6')">
      <div class="model-item-info">
        <div class="model-item-name">Claude Sonnet 4.6 <span class="model-item-badge">RECOMMENDED</span></div>
        <div class="model-item-desc">Cepat, cerdas, ideal untuk semua tugas</div>
      </div>
      <i class="ti ti-check model-check"></i>
    </div>
    <div class="model-item" onclick="selectModel('claude-haiku-4-5-20251001','Claude Haiku 4.5')">
      <div class="model-item-info">
        <div class="model-item-name">Claude Haiku 4.5 <span class="model-item-badge" style="background:rgba(34,197,94,.12);color:#86EFAC">CEPAT</span></div>
        <div class="model-item-desc">Ultra cepat, hemat, untuk tugas ringan</div>
      </div>
      <i class="ti ti-check model-check"></i>
    </div>
    <div class="model-item" onclick="selectModel('claude-opus-4-6','Claude Opus 4.6')">
      <div class="model-item-info">
        <div class="model-item-name">Claude Opus 4.6 <span class="model-item-badge" style="background:rgba(245,158,11,.12);color:#FCD34D">POWERFUL</span></div>
        <div class="model-item-desc">Paling cerdas untuk tugas kompleks</div>
      </div>
      <i class="ti ti-check model-check"></i>
    </div>
  </div>
</div>

<!-- TOAST -->
<div class="toast" id="toast">
  <span class="toast-icon" id="toast-icon"></span>
  <span id="toast-msg"></span>
</div>

<script>
/* ─────────────────────────────────────
   NOVA AI — Full App Script
   Engine: Anthropic Claude API
   Storage: localStorage (per-user)
───────────────────────────────────── */

const API_URL = 'https://api.anthropic.com/v1/messages';
let currentModel = 'claude-sonnet-4-6';
let currentChatId = null;
let isLoading = false;
let currentUser = null;
let authMode = 'login';

// ── STORAGE ──
function loadData(key) {
  try { return JSON.parse(localStorage.getItem(key) || 'null'); } catch { return null; }
}
function saveData(key, val) {
  try { localStorage.setItem(key, JSON.stringify(val)); } catch {}
}
function getUsers() { return loadData('nova_users') || {}; }
function saveUsers(u) { saveData('nova_users', u); }
function getUserHistory(uid) { return loadData('nova_history_' + uid) || []; }
function saveUserHistory(uid, h) { saveData('nova_history_' + uid, h); }

// ── AUTH ──
function switchTab(mode) {
  authMode = mode;
  document.getElementById('tab-login').className = 'auth-tab' + (mode === 'login' ? ' active' : '');
  document.getElementById('tab-register').className = 'auth-tab' + (mode === 'register' ? ' active' : '');
  document.getElementById('field-name').style.display = mode === 'register' ? 'block' : 'none';
  document.getElementById('auth-title').textContent = mode === 'login' ? 'Selamat datang kembali' : 'Buat akun baru';
  document.getElementById('auth-sub').textContent = mode === 'login' ? 'Masuk untuk melanjutkan percakapanmu' : 'Bergabung dan mulai chatting';
  document.getElementById('auth-btn').textContent = mode === 'login' ? 'Masuk' : 'Daftar';
  document.getElementById('auth-error').style.display = 'none';
}

function showAuthError(msg) {
  const el = document.getElementById('auth-error');
  el.textContent = msg;
  el.style.display = 'block';
}

function doAuth() {
  const email = document.getElementById('auth-email').value.trim();
  const pass = document.getElementById('auth-pass').value;
  const name = document.getElementById('auth-name').value.trim();
  document.getElementById('auth-error').style.display = 'none';
  if (!email || !pass) { showAuthError('Email dan password wajib diisi.'); return; }
  const users = getUsers();
  if (authMode === 'register') {
    if (!name) { showAuthError('Nama wajib diisi.'); return; }
    if (users[email]) { showAuthError('Email sudah terdaftar.'); return; }
    if (pass.length < 6) { showAuthError('Password minimal 6 karakter.'); return; }
    users[email] = { name, pass, created: Date.now() };
    saveUsers(users);
    loginUser({ email, name });
  } else {
    if (!users[email] || users[email].pass !== pass) { showAuthError('Email atau password salah.'); return; }
    loginUser({ email, name: users[email].name });
  }
}

function demoLogin() {
  loginUser({ email: 'demo@novaai.id', name: 'Demo User' });
}

function loginUser(user) {
  currentUser = user;
  saveData('nova_session', user);
  document.getElementById('auth-screen').style.display = 'none';
  document.getElementById('app').classList.remove('hidden');
  initApp();
}

function logout() {
  saveData('nova_session', null);
  currentUser = null;
  location.reload();
}

// ── APP INIT ──
function initApp() {
  const initials = (currentUser.name || 'U').split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2);
  document.getElementById('user-avatar').textContent = initials;
  document.getElementById('user-name-display').textContent = currentUser.name || currentUser.email;
  renderChatList();
  newChat();
}

// ── CHAT MANAGEMENT ──
function getChats() { return getUserHistory(currentUser.email); }
function saveChats(c) { saveUserHistory(currentUser.email, c); }

function newChat() {
  currentChatId = 'chat_' + Date.now();
  const chats = getChats();
  chats.unshift({ id: currentChatId, title: 'Chat Baru', messages: [], created: Date.now(), model: currentModel });
  saveChats(chats);
  renderChatList();
  renderMessages([]);
  document.getElementById('chat-header-title').textContent = 'Chat Baru';
  document.getElementById('chat-input').focus();
  closeDropdowns();
}

function loadChat(id) {
  closeDropdowns();
  currentChatId = id;
  const chat = getChats().find(c => c.id === id);
  if (!chat) return;
  document.getElementById('chat-header-title').textContent = chat.title;
  if (chat.model) selectModel(chat.model, chat.model, true);
  renderMessages(chat.messages);
  renderChatList();
}

function deleteChat(id, e) {
  e.stopPropagation();
  const chats = getChats().filter(c => c.id !== id);
  saveChats(chats);
  if (currentChatId === id) newChat();
  else renderChatList();
  showToast('Chat dihapus', 'ti-trash');
}

function renameChat(id, e) {
  e.stopPropagation();
  const name = prompt('Nama chat baru:');
  if (!name) return;
  const chats = getChats();
  const chat = chats.find(c => c.id === id);
  if (chat) {
    chat.title = name;
    saveChats(chats);
    renderChatList();
    if (currentChatId === id) document.getElementById('chat-header-title').textContent = name;
  }
}

function filterChats() {
  const q = document.getElementById('search-input').value.toLowerCase();
  const chats = getChats().filter(c =>
    c.title.toLowerCase().includes(q) ||
    c.messages.some(m => m.content.toLowerCase().includes(q))
  );
  renderChatList(chats);
}

function renderChatList(chats) {
  chats = chats || getChats();
  const el = document.getElementById('chat-list');
  if (!chats.length) {
    el.innerHTML = '<div style="padding:20px;text-align:center;color:var(--fg3);font-size:13px">Belum ada percakapan</div>';
    return;
  }
  const groups = {};
  const now = Date.now();
  chats.forEach(c => {
    const diff = now - c.created;
    let g = 'Lama';
    if (diff < 86400000) g = 'Hari Ini';
    else if (diff < 604800000) g = 'Minggu Ini';
    else if (diff < 2592000000) g = 'Bulan Ini';
    (groups[g] = groups[g] || []).push(c);
  });
  const order = ['Hari Ini', 'Minggu Ini', 'Bulan Ini', 'Lama'];
  el.innerHTML = order.filter(g => groups[g]).map(g => `
    <div class="sidebar-section">${g}</div>
    ${groups[g].map(c => `
    <div class="chat-item${c.id === currentChatId ? ' active' : ''}" onclick="loadChat('${c.id}')">
      <div class="chat-item-icon"><i class="ti ti-message-circle"></i></div>
      <div class="chat-item-info">
        <div class="chat-item-title">${escapeHtml(c.title)}</div>
        <div class="chat-item-meta">${c.messages.length} pesan</div>
      </div>
      <div class="chat-item-actions">
        <button class="chat-item-btn" onclick="renameChat('${c.id}',event)" title="Rename"><i class="ti ti-pencil"></i></button>
        <button class="chat-item-btn del" onclick="deleteChat('${c.id}',event)" title="Hapus"><i class="ti ti-trash"></i></button>
      </div>
    </div>`).join('')}
  `).join('');
}

// ── RENDER MESSAGES ──
function renderMessages(messages) {
  const el = document.getElementById('messages-inner');
  if (!messages.length) {
    el.innerHTML = `<div class="empty-state" id="empty-state">
      <div class="empty-icon"><i class="ti ti-sparkles"></i></div>
      <div class="empty-title">Halo! Saya NOVA.</div>
      <div class="empty-sub">AI assistant yang siap membantu kamu kapan saja. Tanya apa saja — dari kode, cerita, hingga analisis data.</div>
      <div class="suggestion-grid">
        <button class="suggestion" onclick="useSuggestion('Jelaskan konsep machine learning dengan sederhana')"><strong>📚 Belajar</strong>Jelaskan machine learning dengan sederhana</button>
        <button class="suggestion" onclick="useSuggestion('Buat cerita pendek tentang petualangan di luar angkasa')"><strong>✍️ Kreatif</strong>Tulis cerita petualangan luar angkasa</button>
        <button class="suggestion" onclick="useSuggestion('Bantu saya debug kode Python ini')"><strong>💻 Coding</strong>Debug kode Python saya</button>
        <button class="suggestion" onclick="useSuggestion('Buat rencana belajar bahasa Inggris selama 30 hari')"><strong>📋 Rencana</strong>Rencana belajar bahasa Inggris 30 hari</button>
      </div>
    </div>`;
    return;
  }
  el.innerHTML = messages.map(m => `
    <div class="msg-wrap ${m.role === 'user' ? 'user' : ''}">
      <div class="msg-avatar ${m.role === 'user' ? 'user-av' : 'ai'}">
        ${m.role === 'user' ? '<i class="ti ti-user" style="font-size:14px"></i>' : '<i class="ti ti-sparkles" style="font-size:14px"></i>'}
      </div>
      <div class="msg-content">
        <div class="bubble ${m.role === 'user' ? 'user-b' : 'ai'}">${m.role === 'user' ? escapeHtml(m.content) : markdownToHtml(m.content)}</div>
        <div class="msg-meta">
          <span class="msg-time">${m.time || ''}</span>
          <div class="msg-actions">
            <button class="msg-action-btn" onclick="copyMsg(this,'${encodeURIComponent(m.content)}')">
              <i class="ti ti-copy" style="font-size:12px"></i>Salin
            </button>
          </div>
        </div>
      </div>
    </div>
  `).join('');
  scrollBottom();
}

// ── SEND MESSAGE ──
async function sendMessage() {
  const input = document.getElementById('chat-input');
  const text = input.value.trim();
  if (!text || isLoading) return;
  isLoading = true;
  document.getElementById('send-btn').disabled = true;
  input.value = '';
  autoResize(input);
  document.getElementById('empty-state')?.remove();
  addMessage('user', text);
  renderCurrentMessages();
  showTyping();
  try {
    const chats = getChats();
    const chat = chats.find(c => c.id === currentChatId);
    const history = (chat?.messages || []).slice(-20).map(m => ({ role: m.role, content: m.content }));
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: currentModel,
        max_tokens: 1000,
        system: 'Kamu adalah NOVA, AI assistant cerdas dan ramah berbahasa Indonesia. Jawab dengan akurat, helpful, dan natural. Gunakan format markdown jika membantu kejelasan.',
        messages: history
      })
    });
    const data = await res.json();
    if (data.error) throw new Error(data.error.message || 'API Error');
    const reply = data.content?.[0]?.text || 'Maaf, saya tidak bisa menjawab saat ini.';
    hideTyping();
    addMessage('assistant', reply);
    renderCurrentMessages();
    const updated = getChats().find(c => c.id === currentChatId);
    document.getElementById('chat-header-title').textContent = updated?.title || 'Chat';
  } catch (err) {
    hideTyping();
    addMessage('assistant', '⚠️ Terjadi kesalahan: ' + err.message);
    renderCurrentMessages();
  }
  isLoading = false;
  document.getElementById('send-btn').disabled = false;
  input.focus();
}

function addMessage(role, content) {
  const chats = getChats();
  const chat = chats.find(c => c.id === currentChatId);
  if (!chat) return;
  const msg = { role, content, time: timeStr() };
  chat.messages.push(msg);
  if (chat.messages.length === 2 && role === 'assistant') {
    chat.title = chat.messages[0].content.slice(0, 45) + (chat.messages[0].content.length > 45 ? '…' : '');
  }
  saveChats(chats);
  renderChatList();
}

function renderCurrentMessages() {
  const chat = getChats().find(c => c.id === currentChatId);
  if (chat) renderMessages(chat.messages);
}

function showTyping() {
  const el = document.getElementById('messages-inner');
  const div = document.createElement('div');
  div.id = 'typing-indicator';
  div.className = 'msg-wrap';
  div.innerHTML = `<div class="msg-avatar ai"><i class="ti ti-sparkles" style="font-size:14px"></i></div>
    <div class="bubble ai"><div class="typing"><span></span><span></span><span></span></div></div>`;
  el.appendChild(div);
  scrollBottom();
}

function hideTyping() {
  document.getElementById('typing-indicator')?.remove();
}

function scrollBottom() {
  setTimeout(() => {
    const m = document.getElementById('messages');
    m.scrollTop = m.scrollHeight;
  }, 50);
}

// ── INPUT UTILS ──
function handleKey(e) {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
}

function autoResize(el) {
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 140) + 'px';
  document.getElementById('send-btn').disabled = !el.value.trim();
}

function useSuggestion(text) {
  document.getElementById('chat-input').value = text;
  autoResize(document.getElementById('chat-input'));
  sendMessage();
}

function timeStr() {
  return new Date().toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' });
}

function escapeHtml(t) {
  return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function markdownToHtml(text) {
  return escapeHtml(text)
    .replace(/```(\w+)?\n?([\s\S]*?)```/g, '<pre><code>$2</code></pre>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/^\- (.+)$/gm, '<li>$1</li>')
    .replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>')
    .replace(/^\d+\. (.+)$/gm, '<li>$1</li>')
    .replace(/^&gt; (.+)$/gm, '<blockquote>$1</blockquote>')
    .replace(/\n\n/g, '</p><p>')
    .replace(/\n/g, '<br>')
    .replace(/^(?!<[hupblo])/, '<p>')
    .replace(/(?<![>])$/, '</p>');
}

function copyMsg(btn, encoded) {
  navigator.clipboard.writeText(decodeURIComponent(encoded)).then(() => {
    const orig = btn.innerHTML;
    btn.innerHTML = '<i class="ti ti-check" style="font-size:12px"></i>Tersalin';
    setTimeout(() => { btn.innerHTML = orig; }, 2000);
  });
}

// ── DROPDOWNS ──
function toggleModelPicker() {
  document.getElementById('model-picker').classList.toggle('open');
  document.getElementById('user-dropdown').classList.remove('open');
}

function selectModel(model, label, silent) {
  currentModel = model;
  document.getElementById('model-label').textContent = model;
  document.querySelectorAll('.model-item').forEach(el => {
    el.classList.toggle('active', el.getAttribute('onclick')?.includes("'" + model + "'"));
  });
  document.getElementById('model-picker').classList.remove('open');
  if (!silent) showToast('Model: ' + model, 'ti-robot');
}

function toggleUserMenu() {
  document.getElementById('user-dropdown').classList.toggle('open');
  document.getElementById('model-picker').classList.remove('open');
}

function closeDropdowns() {
  document.getElementById('model-picker').classList.remove('open');
  document.getElementById('user-dropdown').classList.remove('open');
}

// ── ACTIONS ──
function clearCurrentChat() {
  if (!confirm('Hapus semua pesan di chat ini?')) return;
  const chats = getChats();
  const chat = chats.find(c => c.id === currentChatId);
  if (chat) { chat.messages = []; saveChats(chats); renderMessages([]); showToast('Chat dibersihkan', 'ti-eraser'); }
}

function clearAllChats() {
  if (!confirm('Hapus SEMUA percakapan? Ini tidak bisa dibatalkan.')) return;
  saveChats([]);
  newChat();
  showToast('Semua chat dihapus', 'ti-trash');
  document.getElementById('user-dropdown').classList.remove('open');
}

function exportChats() {
  const data = JSON.stringify(getChats(), null, 2);
  const a = document.createElement('a');
  a.href = 'data:text/json;charset=utf-8,' + encodeURIComponent(data);
  a.download = 'nova-chat-export.json';
  a.click();
  showToast('Chat diekspor', 'ti-download');
  document.getElementById('user-dropdown').classList.remove('open');
}

function shareChat() { showToast('Link disalin ke clipboard', 'ti-share'); }

function showToast(msg, icon) {
  const t = document.getElementById('toast');
  document.getElementById('toast-msg').textContent = msg;
  document.getElementById('toast-icon').className = 'toast-icon ti ' + icon;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2500);
}

// ── CLOSE ON OUTSIDE CLICK ──
document.addEventListener('click', e => {
  if (!e.target.closest('.model-badge') && !e.target.closest('.model-picker'))
    document.getElementById('model-picker').classList.remove('open');
  if (!e.target.closest('.user-card') && !e.target.closest('.user-dropdown'))
    document.getElementById('user-dropdown').classList.remove('open');
});

// ── BOOT ──
window.addEventListener('load', () => {
  const session = loadData('nova_session');
  if (session && session.email) {
    currentUser = session;
    document.getElementById('auth-screen').style.display = 'none';
    document.getElementById('app').classList.remove('hidden');
    initApp();
  }
});
</script>
</body>
</html>
