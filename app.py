import streamlit as st
import anthropic
import json
import hashlib
import os
from datetime import datetime
from pathlib import Path

# ─────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="NOVA AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATA_DIR = Path("nova_data")
DATA_DIR.mkdir(exist_ok=True)
USERS_FILE = DATA_DIR / "users.json"
CHATS_DIR = DATA_DIR / "chats"
CHATS_DIR.mkdir(exist_ok=True)

MODELS = {
    "claude-sonnet-4-6": "Claude Sonnet 4.6 — Cepat & Cerdas ⭐",
    "claude-haiku-4-5-20251001": "Claude Haiku 4.5 — Ultra Cepat ⚡",
    "claude-opus-4-6": "Claude Opus 4.6 — Paling Powerful 🧠",
}

# ─────────────────────────────────────────
# CSS
# ─────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
/* ── GLOBAL ── */
html, body, [data-testid="stApp"],
[data-testid="stAppViewContainer"] {
    background: #0A0A0B !important;
    color: #FAFAFA !important;
    font-family: 'Inter', sans-serif !important;
}
.block-container { padding-top: 0 !important; max-width: 100% !important; }
#MainMenu, footer, header,
[data-testid="stDecoration"],
[data-testid="stDeployButton"] { display: none !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: #111113 !important;
    border-right: 1px solid rgba(255,255,255,0.08) !important;
}
[data-testid="stSidebar"] * { color: #FAFAFA !important; font-family: 'Inter', sans-serif !important; }

/* Sidebar buttons */
[data-testid="stSidebar"] .stButton > button {
    width: 100% !important;
    background: transparent !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #A1A1AA !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 8px 12px !important;
    border-radius: 10px !important;
    text-align: left !important;
    transition: all .2s !important;
    margin-bottom: 2px !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(124,58,237,0.1) !important;
    border-color: #7C3AED !important;
    color: #C4B5FD !important;
}
[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: rgba(124,58,237,0.15) !important;
    border-color: rgba(124,58,237,0.4) !important;
    color: #C4B5FD !important;
}

/* ── MAIN ── */
[data-testid="stMainBlockContainer"] {
    background: #0A0A0B !important;
    padding: 0 !important;
}

/* ── CHAT MESSAGES ── */
[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    padding: 4px 0 !important;
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) .stMarkdown {
    background: #18181B !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 4px 16px 16px 16px !important;
    padding: 12px 16px !important;
    font-size: 14px !important;
    line-height: 1.7 !important;
    color: #FAFAFA !important;
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    flex-direction: row-reverse !important;
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) .stMarkdown {
    background: #7C3AED !important;
    border-radius: 16px 16px 4px 16px !important;
    padding: 12px 16px !important;
    font-size: 14px !important;
    line-height: 1.7 !important;
    color: #fff !important;
}
[data-testid="chatAvatarIcon-assistant"] {
    background: #7C3AED !important;
    border-radius: 50% !important;
    color: #fff !important;
}
[data-testid="chatAvatarIcon-user"] {
    background: #222228 !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 50% !important;
    color: #A1A1AA !important;
}

/* ── CODE BLOCKS ── */
code, pre {
    font-family: 'JetBrains Mono', monospace !important;
    background: #0A0A0B !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    color: #C4B5FD !important;
    font-size: 13px !important;
}

/* ── CHAT INPUT ── */
[data-testid="stChatInputContainer"] {
    background: #111113 !important;
    border-top: 1px solid rgba(255,255,255,0.08) !important;
    padding: 12px 20px !important;
}
[data-testid="stChatInputContainer"] textarea {
    background: #18181B !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    color: #FAFAFA !important;
    border-radius: 12px !important;
    font-size: 14px !important;
    font-family: 'Inter', sans-serif !important;
}
[data-testid="stChatInputContainer"] textarea:focus {
    border-color: #7C3AED !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.15) !important;
}
[data-testid="stChatInputContainer"] textarea::placeholder { color: #52525B !important; }
[data-testid="stChatInputContainer"] button {
    background: #7C3AED !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
}
[data-testid="stChatInputContainer"] button:hover { background: #9B59F5 !important; }

/* ── SELECTBOX ── */
[data-testid="stSelectbox"] > div > div {
    background: #18181B !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    color: #FAFAFA !important;
    border-radius: 10px !important;
}
[data-testid="stSelectbox"] label { color: #A1A1AA !important; font-size: 12px !important; }

/* ── TEXT INPUT ── */
.stTextInput input, .stTextArea textarea {
    background: #18181B !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    color: #FAFAFA !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #7C3AED !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.15) !important;
}
.stTextInput input::placeholder,
.stTextArea textarea::placeholder { color: #52525B !important; }
.stTextInput label, .stTextArea label {
    color: #A1A1AA !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    letter-spacing: .04em !important;
    text-transform: uppercase !important;
}

/* ── FORM SUBMIT BUTTON ── */
.stForm .stButton > button {
    background: #7C3AED !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    width: 100% !important;
    padding: 10px !important;
}
.stForm .stButton > button:hover { background: #9B59F5 !important; }

/* ── DIVIDER ── */
hr { border-color: rgba(255,255,255,0.08) !important; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #222228; border-radius: 4px; }

/* ── ALERTS ── */
[data-testid="stAlert"] { border-radius: 10px !important; }

/* ── SPINNER ── */
[data-testid="stSpinner"] { color: #7C3AED !important; }

/* ── TABS ── */
[data-testid="stTabs"] [role="tab"] {
    color: #A1A1AA !important;
    font-weight: 500 !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    color: #C4B5FD !important;
    border-bottom-color: #7C3AED !important;
}

/* ── CUSTOM CARDS ── */
.nova-header {
    background: linear-gradient(135deg, #111113 0%, #18181B 100%);
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding: 18px 24px;
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 0;
}
.nova-logo {
    font-size: 28px;
    font-weight: 800;
    letter-spacing: -.03em;
    color: #FAFAFA;
}
.nova-logo span { color: #7C3AED; }
.nova-tagline { font-size: 12px; color: #52525B; margin-top: 2px; }
.chat-item-active {
    background: rgba(124,58,237,0.12) !important;
    border: 1px solid rgba(124,58,237,0.3) !important;
    border-radius: 10px !important;
    padding: 8px 10px !important;
}
.empty-hint {
    text-align: center;
    padding: 60px 20px;
    color: #52525B;
}
.empty-hint h2 { font-size: 20px; color: #A1A1AA; margin-bottom: 8px; font-weight: 600; }
.empty-hint p { font-size: 14px; line-height: 1.7; }
.model-info {
    background: #18181B;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 10px 14px;
    font-size: 12px;
    color: #A1A1AA;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
}
.model-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #22C55E;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# DATA HELPERS
# ─────────────────────────────────────────
def load_users():
    if USERS_FILE.exists():
        return json.loads(USERS_FILE.read_text())
    return {}

def save_users(users):
    USERS_FILE.write_text(json.dumps(users, indent=2))

def hash_pass(p):
    return hashlib.sha256(p.encode()).hexdigest()

def get_user_chats_file(email):
    safe = email.replace("@", "_at_").replace(".", "_")
    return CHATS_DIR / f"{safe}.json"

def load_chats(email):
    f = get_user_chats_file(email)
    if f.exists():
        return json.loads(f.read_text())
    return []

def save_chats(email, chats):
    get_user_chats_file(email).write_text(json.dumps(chats, indent=2))

def now_str():
    return datetime.now().strftime("%H:%M")

def date_str():
    return datetime.now().strftime("%d %b %Y")


# ─────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────
def init_state():
    defaults = {
        "logged_in": False,
        "user_email": "",
        "user_name": "",
        "auth_tab": "login",
        "current_chat_id": None,
        "model": "claude-sonnet-4-6",
        "page": "chat",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ─────────────────────────────────────────
# AUTH PAGE
# ─────────────────────────────────────────
def show_auth():
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center;padding:40px 0 24px">
            <div style="font-size:42px;font-weight:800;letter-spacing:-.03em;color:#FAFAFA">
                NO<span style="color:#7C3AED">VA</span>
            </div>
            <div style="font-size:13px;color:#52525B;margin-top:4px">AI Assistant · Powered by Claude</div>
        </div>
        """, unsafe_allow_html=True)

        tab_login, tab_reg = st.tabs(["🔑  Masuk", "✨  Daftar"])

        with tab_login:
            with st.form("form_login"):
                email = st.text_input("Email", placeholder="kamu@email.com", key="li_email")
                password = st.text_input("Password", type="password", placeholder="••••••••", key="li_pass")
                submitted = st.form_submit_button("Masuk →")
                if submitted:
                    users = load_users()
                    if email in users and users[email]["pass"] == hash_pass(password):
                        st.session_state.logged_in = True
                        st.session_state.user_email = email
                        st.session_state.user_name = users[email]["name"]
                        st.rerun()
                    else:
                        st.error("Email atau password salah.")

            st.markdown('<div style="text-align:center;margin-top:12px">', unsafe_allow_html=True)
            if st.button("⚡ Demo — Langsung Coba", use_container_width=True):
                st.session_state.logged_in = True
                st.session_state.user_email = "demo@novaai.id"
                st.session_state.user_name = "Demo User"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        with tab_reg:
            with st.form("form_reg"):
                name = st.text_input("Nama", placeholder="Nama kamu", key="reg_name")
                email_r = st.text_input("Email", placeholder="kamu@email.com", key="reg_email")
                pass_r = st.text_input("Password", type="password", placeholder="Min. 6 karakter", key="reg_pass")
                submitted_r = st.form_submit_button("Daftar →")
                if submitted_r:
                    if not name or not email_r or not pass_r:
                        st.error("Semua field wajib diisi.")
                    elif len(pass_r) < 6:
                        st.error("Password minimal 6 karakter.")
                    else:
                        users = load_users()
                        if email_r in users:
                            st.error("Email sudah terdaftar.")
                        else:
                            users[email_r] = {"name": name, "pass": hash_pass(pass_r), "created": date_str()}
                            save_users(users)
                            st.session_state.logged_in = True
                            st.session_state.user_email = email_r
                            st.session_state.user_name = name
                            st.rerun()


# ─────────────────────────────────────────
# CHAT PAGE
# ─────────────────────────────────────────
def show_chat():
    email = st.session_state.user_email
    name = st.session_state.user_name

    # ── SIDEBAR ──
    with st.sidebar:
        st.markdown(f"""
        <div style="padding:8px 0 16px">
            <div style="font-size:22px;font-weight:800;letter-spacing:-.03em;color:#FAFAFA">
                NO<span style="color:#7C3AED">VA</span>
            </div>
            <div style="font-size:11px;color:#52525B;margin-top:2px">Powered by Claude</div>
        </div>
        """, unsafe_allow_html=True)

        # New chat button
        if st.button("✏️  Chat Baru", use_container_width=True):
            new_chat_id = f"chat_{int(datetime.now().timestamp() * 1000)}"
            chats = load_chats(email)
            chats.insert(0, {
                "id": new_chat_id,
                "title": "Chat Baru",
                "messages": [],
                "created": date_str(),
                "model": st.session_state.model,
            })
            save_chats(email, chats)
            st.session_state.current_chat_id = new_chat_id
            st.rerun()

        st.divider()

        # Model selector
        st.selectbox(
            "Model AI",
            options=list(MODELS.keys()),
            format_func=lambda x: MODELS[x],
            key="model"
        )

        st.divider()

        # Chat history list
        chats = load_chats(email)
        if chats:
            st.markdown('<div style="font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#52525B;margin-bottom:8px">Riwayat</div>', unsafe_allow_html=True)

            # Search
            search = st.text_input("", placeholder="🔍  Cari percakapan...", label_visibility="collapsed")

            filtered = [c for c in chats if search.lower() in c["title"].lower() or
                        any(search.lower() in m["content"].lower() for m in c.get("messages", []))] if search else chats

            for chat in filtered[:30]:
                cid = chat["id"]
                is_active = cid == st.session_state.current_chat_id
                n_msg = len(chat.get("messages", []))
                label = f"{'▪ ' if is_active else ''}{chat['title'][:32]}"
                col_a, col_b = st.columns([5, 1])
                with col_a:
                    if st.button(label, key=f"chat_{cid}", type="primary" if is_active else "secondary", use_container_width=True):
                        st.session_state.current_chat_id = cid
                        st.rerun()
                with col_b:
                    if st.button("🗑", key=f"del_{cid}", help="Hapus chat"):
                        chats = [c for c in chats if c["id"] != cid]
                        save_chats(email, chats)
                        if st.session_state.current_chat_id == cid:
                            st.session_state.current_chat_id = chats[0]["id"] if chats else None
                        st.rerun()
        else:
            st.caption("Belum ada percakapan")

        st.divider()

        # User info
        initials = "".join([w[0].upper() for w in (name or "U").split()][:2])
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;padding:8px 4px">
            <div style="width:32px;height:32px;border-radius:50%;background:#7C3AED;
                        display:flex;align-items:center;justify-content:center;
                        font-size:13px;font-weight:600;color:#fff;flex-shrink:0">{initials}</div>
            <div>
                <div style="font-size:13px;font-weight:500">{name}</div>
                <div style="font-size:11px;color:#52525B">{email}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚪  Keluar", use_container_width=True):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

        if chats:
            if st.button("📥  Export JSON", use_container_width=True):
                st.download_button(
                    "Download",
                    data=json.dumps(chats, indent=2),
                    file_name="nova-chats.json",
                    mime="application/json",
                    use_container_width=True
                )

    # ── MAIN CHAT AREA ──
    chats = load_chats(email)

    # Auto-create first chat
    if not st.session_state.current_chat_id or not any(c["id"] == st.session_state.current_chat_id for c in chats):
        if chats:
            st.session_state.current_chat_id = chats[0]["id"]
        else:
            new_id = f"chat_{int(datetime.now().timestamp() * 1000)}"
            chats = [{"id": new_id, "title": "Chat Baru", "messages": [], "created": date_str(), "model": st.session_state.model}]
            save_chats(email, chats)
            st.session_state.current_chat_id = new_id

    current_chat = next((c for c in chats if c["id"] == st.session_state.current_chat_id), chats[0])
    messages = current_chat.get("messages", [])

    # Header
    st.markdown(f"""
    <div style="background:#111113;border-bottom:1px solid rgba(255,255,255,0.08);
                padding:14px 20px;display:flex;align-items:center;gap:12px;margin-bottom:0">
        <div style="display:flex;align-items:center;gap:8px;background:#18181B;
                    border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:5px 12px">
            <span style="width:7px;height:7px;border-radius:50%;background:#22C55E;display:inline-block"></span>
            <span style="font-size:12px;font-weight:500;color:#A1A1AA">{st.session_state.model}</span>
        </div>
        <div style="font-size:14px;font-weight:500;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">
            {current_chat['title']}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Empty state
    if not messages:
        st.markdown("""
        <div class="empty-hint">
            <div style="font-size:48px;margin-bottom:16px">⚡</div>
            <h2>Halo! Saya NOVA.</h2>
            <p>AI assistant yang siap membantu kamu kapan saja.<br>
            Tanya apa saja — kode, cerita, matematika, terjemahan, analisis, dan lainnya.</p>
        </div>
        """, unsafe_allow_html=True)

        # Suggestion chips
        suggestions = [
            ("📚", "Jelaskan machine learning dengan sederhana"),
            ("✍️", "Buat cerita pendek tentang petualangan di hutan"),
            ("💻", "Contoh REST API dengan FastAPI Python"),
            ("📋", "Buat rencana belajar bahasa Inggris 30 hari"),
        ]
        cols = st.columns(2)
        for i, (icon, sug) in enumerate(suggestions):
            with cols[i % 2]:
                if st.button(f"{icon} {sug}", key=f"sug_{i}", use_container_width=True):
                    _send_message(sug, current_chat, chats, email)

    # Render messages
    for msg in messages:
        with st.chat_message(msg["role"], avatar="⚡" if msg["role"] == "assistant" else "👤"):
            st.markdown(msg["content"])
            st.caption(msg.get("time", ""))

    # Chat input
    if prompt := st.chat_input("Ketik pesan... (Enter kirim, Shift+Enter baris baru)"):
        _send_message(prompt, current_chat, chats, email)


def _send_message(prompt, current_chat, chats, email):
    """Kirim pesan ke Claude dan simpan hasilnya."""
    # Tampilkan pesan user
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Simpan pesan user
    current_chat["messages"].append({
        "role": "user",
        "content": prompt,
        "time": now_str()
    })

    # Auto-rename chat dari pesan pertama
    if len(current_chat["messages"]) == 1:
        current_chat["title"] = prompt[:45] + ("…" if len(prompt) > 45 else "")

    # Update model di chat
    current_chat["model"] = st.session_state.model

    # Panggil Claude API
    with st.chat_message("assistant", avatar="⚡"):
        with st.spinner(""):
            try:
                api_key = os.getenv("ANTHROPIC_API_KEY")
                if not api_key:
                    st.error("⚠️ ANTHROPIC_API_KEY tidak ditemukan di environment variable.")
                    return

                client = anthropic.Anthropic(api_key=api_key)

                # Ambil context (max 20 pesan terakhir)
                history = [
                    {"role": m["role"], "content": m["content"]}
                    for m in current_chat["messages"][-20:]
                ]

                response = client.messages.create(
                    model=st.session_state.model,
                    max_tokens=2048,
                    system=(
                        "Kamu adalah NOVA, AI assistant cerdas dan ramah berbahasa Indonesia. "
                        "Jawab dengan akurat, helpful, dan natural. "
                        "Gunakan format markdown jika membantu kejelasan jawaban. "
                        "Berikan jawaban yang komprehensif tapi tetap to the point."
                    ),
                    messages=history,
                )
                reply = response.content[0].text

            except anthropic.AuthenticationError:
                reply = "⚠️ API key tidak valid. Periksa `ANTHROPIC_API_KEY` kamu."
            except anthropic.RateLimitError:
                reply = "⚠️ Rate limit tercapai. Coba beberapa saat lagi."
            except Exception as e:
                reply = f"⚠️ Terjadi kesalahan: {str(e)}"

            st.markdown(reply)
            st.caption(now_str())

    # Simpan balasan
    current_chat["messages"].append({
        "role": "assistant",
        "content": reply,
        "time": now_str()
    })

    # Update & simpan chats
    for i, c in enumerate(chats):
        if c["id"] == current_chat["id"]:
            chats[i] = current_chat
            break

    save_chats(email, chats)
    st.rerun()


# ─────────────────────────────────────────
# ROUTER
# ─────────────────────────────────────────
if not st.session_state.logged_in:
    show_auth()
else:
    show_chat()
