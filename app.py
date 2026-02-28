import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from datetime import date, timedelta

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ─── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="TripMate – Student Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS (Light Theme) ────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap');

  html, body, [class*="css"] {
      font-family: 'DM Sans', sans-serif;
      background: #f5f7fa;
      color: #1a1a2e;
  }
  .stApp { background: #f5f7fa; }

  /* Hero Banner */
  .hero {
      background: linear-gradient(135deg, #1a73e8 0%, #0d47a1 60%, #1565c0 100%);
      border-radius: 20px;
      padding: 3rem 2rem;
      text-align: center;
      margin-bottom: 2rem;
      box-shadow: 0 8px 32px rgba(26,115,232,0.25);
  }
  .hero h1 {
      font-family: 'Playfair Display', serif;
      font-size: 3.5rem;
      font-weight: 900;
      color: #ffffff;
      margin: 0;
      letter-spacing: -1px;
  }
  .hero p {
      color: #cce0ff;
      font-size: 1.1rem;
      margin-top: 0.5rem;
  }

  /* Section Titles */
  .section-title {
      font-family: 'Playfair Display', serif;
      font-size: 1.2rem;
      color: #1a73e8;
      border-bottom: 2px solid #e8f0fe;
      padding-bottom: 0.5rem;
      margin-bottom: 1.2rem;
  }

  /* Inputs */
  .stTextInput > div > div > input,
  .stNumberInput > div > div > input,
  .stSelectbox > div > div,
  .stDateInput > div > div > input,
  .stMultiSelect > div > div {
      background: #ffffff !important;
      border: 1.5px solid #d0d7e2 !important;
      border-radius: 10px !important;
      color: #1a1a2e !important;
      font-family: 'DM Sans', sans-serif !important;
  }
  .stTextInput > div > div > input:focus,
  .stNumberInput > div > div > input:focus {
      border-color: #1a73e8 !important;
      box-shadow: 0 0 0 3px rgba(26,115,232,0.12) !important;
  }
  label { color: #444f6b !important; font-size: 0.85rem !important; font-weight: 500 !important; }

  /* Button */
  .stButton > button {
      background: linear-gradient(135deg, #1a73e8, #0d47a1) !important;
      color: #ffffff !important;
      font-family: 'DM Sans', sans-serif !important;
      font-weight: 700 !important;
      font-size: 1rem !important;
      border: none !important;
      border-radius: 50px !important;
      padding: 0.75rem 3rem !important;
      width: 100% !important;
      transition: all 0.3s ease !important;
      letter-spacing: 0.5px !important;
  }
  .stButton > button:hover {
      transform: translateY(-2px) !important;
      box-shadow: 0 8px 25px rgba(26,115,232,0.4) !important;
  }

  /* Itinerary Output */
  .itinerary-box {
      background: #ffffff;
      border: 1.5px solid #d0d7e2;
      border-radius: 16px;
      padding: 2rem;
      margin-top: 1.5rem;
      line-height: 1.8;
      box-shadow: 0 4px 16px rgba(0,0,0,0.06);
  }
  .itinerary-box h3 {
      font-family: 'Playfair Display', serif;
      color: #1a73e8;
  }

  /* Tags */
  .tag {
      display: inline-block;
      background: #e8f0fe;
      border: 1px solid #bbd0f8;
      color: #1a73e8;
      border-radius: 20px;
      padding: 3px 12px;
      font-size: 0.78rem;
      margin: 3px;
      font-weight: 500;
  }

  /* Tips card */
  .tip-card {
      background: #f0f6ff;
      border-left: 4px solid #1a73e8;
      border-radius: 0 10px 10px 0;
      padding: 1rem 1.2rem;
      margin-top: 1rem;
      font-size: 0.9rem;
      color: #2c3e6b;
  }
  .tip-card a { color: #1a73e8; }

  /* Divider */
  hr { border-color: #e0e6f0 !important; }

  /* Spinner */
  .stSpinner > div { border-top-color: #1a73e8 !important; }

  /* Summary bar */
  .summary-bar {
      background: #e8f0fe;
      border-radius: 12px;
      border: 1px solid #bbd0f8;
      padding: 0.8rem 1rem;
      margin: 1rem 0;
  }

  /* Footer */
  .footer { text-align:center; color: #8a95ad; font-size: 0.8rem; padding: 1rem; }
</style>
""", unsafe_allow_html=True)


# ─── Hero Section ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>✈️ TripMate</h1>
  <p>Your AI-Powered Student Travel Planner — Budget Smart, Explore More</p>
</div>
""", unsafe_allow_html=True)


# ─── Form ───────────────────────────────────────────────────────────────────────
with st.form("travel_form"):

    # Row 1 – Source & Destination
    st.markdown('<div class="section-title">🗺️ Journey Details</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        source = st.text_input("📍 Source Location", placeholder="e.g. Chennai, Tamil Nadu")
    with col2:
        destination = st.text_input("🏁 Destination", placeholder="e.g. Goa")

    # Row 2 – Dates & Duration
    col3, col4, col5 = st.columns(3)
    with col3:
        travel_date = st.date_input("🗓️ Travel Start Date", value=date.today() + timedelta(days=7))
    with col4:
        return_date = st.date_input("🔙 Return Date", value=date.today() + timedelta(days=10))
    with col5:
        duration = st.number_input("🌙 Duration (Days)", min_value=1, max_value=30, value=3)

    st.markdown("---")

    # Row 3 – Budget & Transport
    st.markdown('<div class="section-title">💰 Budget & Transport</div>', unsafe_allow_html=True)
    col6, col7 = st.columns(2)
    with col6:
        budget = st.number_input("💵 Total Budget (₹)", min_value=500, max_value=500000, value=15000, step=500)
    with col7:
        transport = st.selectbox("🚌 Mode of Transport", [
            "Train (Recommended – Budget Friendly)",
            "Bus (Economy)",
            "Flight (Low-Cost Carriers)",
            "Road Trip / Self-Drive",
            "Bike / Scooter",
            "Mixed (Train + Local Transport)",
        ])

    st.markdown("---")

    # Row 4 – Interests
    st.markdown('<div class="section-title">🎯 Places & Experiences</div>', unsafe_allow_html=True)
    interests = st.multiselect(
        "What do you want to explore? (Select all that apply)",
        [
            "🏖️ Beaches", "⛪ Temples & Spiritual Sites", "🍜 Street Food & Local Cuisine",
            "🏛️ Museums & Heritage", "🏕️ Trekking & Nature", "🎡 Nightlife & Entertainment",
            "🛍️ Shopping & Markets", "📸 Photography Spots", "🤿 Adventure Sports",
            "☕ Cafés & Hangout Spots", "🚢 Boat Rides & Cruises", "🏞️ Scenic Viewpoints"
        ],
        default=["🏖️ Beaches", "🍜 Street Food & Local Cuisine"]
    )

    extra_notes = st.text_area("📝 Anything specific? (Dietary preferences, accessibility needs, group size, etc.)",
                               placeholder="e.g. Vegetarian food only, group of 4 friends, prefer hostels over hotels...")

    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🚀 Generate My Itinerary")


# ─── AI Generation ──────────────────────────────────────────────────────────────
def generate_itinerary(source, destination, budget, transport, interests, duration, travel_date, return_date, extra_notes):
    interests_clean = [i.split(" ", 1)[1] if " " in i else i for i in interests]

    prompt = f"""
You are TripMate, an expert budget travel planner for Indian college students.

A student wants to travel:
- From: {source}
- To: {destination}
- Travel Date: {travel_date.strftime('%d %B %Y')}
- Return Date: {return_date.strftime('%d %B %Y')}
- Duration: {duration} days
- Total Budget: ₹{budget:,} (Indian Rupees) – this is the TOTAL budget including travel, stay, food, and activities
- Transport Mode: {transport}
- Interests: {', '.join(interests_clean)}
- Special Notes: {extra_notes if extra_notes else 'None'}

Create a DETAILED, PRACTICAL, and BUDGET-CONSCIOUS travel itinerary. Include:

1. **Budget Breakdown** – Estimated cost split for: transport (to & fro), accommodation, food, activities, miscellaneous. Make sure total stays within ₹{budget:,}.

2. **Transport Tips** – Best trains/buses to book, apps to use (IRCTC, RedBus, etc.), approximate ticket costs, booking timing advice.

3. **Where to Stay** – Budget hostel/guesthouse recommendations (₹300–₹800/night), mention platforms like Zostel, Goibibo, MakeMyTrip.

4. **Day-by-Day Itinerary** – For each day:
   - Morning, Afternoon, Evening activities
   - Specific place names with entry fees
   - Food spots with approximate meal costs (₹50–₹200 range for students)
   - Local transport options (auto, bus, shared cab)

5. **Student Hacks** – Discount tips, student ID benefits, free entry places, free WiFi spots, safety tips.

6. **Must-Eat Street Foods** – 5 local dishes and where to find them cheaply.

7. **Packing Checklist** – Essentials for this specific destination/season.

Format the response clearly with emojis and section headers. Be specific with Indian place names, prices in ₹, and practical advice tailored for college students aged 18–24.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are TripMate, an enthusiastic and knowledgeable Indian student travel advisor. You give practical, budget-smart advice with real place names, real prices, and genuine tips. Your tone is friendly, like an experienced traveler friend."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2500,
        temperature=0.8
    )
    return response.choices[0].message.content


# ─── Display Result ──────────────────────────────────────────────────────────────
if submitted:
    if not source or not destination:
        st.error("⚠️ Please enter both Source Location and Destination!")
    elif return_date <= travel_date:
        st.error("⚠️ Return date must be after travel start date!")
    elif not interests:
        st.warning("💡 Tip: Select at least one interest for a better itinerary!")
    else:
        st.markdown(f"""
        <div class="summary-bar">
            <span class="tag">📍 {source} → {destination}</span>
            <span class="tag">🌙 {duration} Days</span>
            <span class="tag">💰 ₹{budget:,}</span>
            <span class="tag">🗓️ {travel_date.strftime('%d %b')} – {return_date.strftime('%d %b %Y')}</span>
        </div>
        """, unsafe_allow_html=True)

        with st.spinner("✨ Crafting your perfect student itinerary..."):
            try:
                itinerary = generate_itinerary(
                    source, destination, budget, transport,
                    interests, duration, travel_date, return_date, extra_notes
                )

                if itinerary:
                    st.markdown('<div class="itinerary-box">', unsafe_allow_html=True)
                    st.markdown(f"### 🗺️ Your Personalised Itinerary: {source} → {destination}")
                    st.markdown(itinerary)
                    st.markdown('</div>', unsafe_allow_html=True)

                    st.markdown("""
                    <div class="tip-card">
                    <strong>🔗 Useful Booking Resources for Students:</strong><br>
                    • <strong>Trains:</strong> <a href="https://www.irctc.co.in">IRCTC</a> |
                      <a href="https://www.confirmtkt.com">ConfirmTkt</a> |
                      <a href="https://www.railyatri.in">RailYatri</a><br>
                    • <strong>Buses:</strong> <a href="https://www.redbus.in">RedBus</a> |
                      <a href="https://www.abhibus.com">AbhiBus</a><br>
                    • <strong>Stays:</strong> <a href="https://www.zostel.com">Zostel</a> |
                      <a href="https://www.goibibo.com">Goibibo</a> |
                      <a href="https://www.oyo.com">OYO</a><br>
                    • <strong>Flights:</strong> <a href="https://www.skyscanner.co.in">Skyscanner</a> |
                      <a href="https://www.ixigo.com">ixigo</a><br>
                    • <strong>Local Travel:</strong>
                      <a href="https://www.rapido.bike">Rapido</a> |
                      <a href="https://www.olacabs.com">Ola</a> | Uber
                    </div>
                    """, unsafe_allow_html=True)

                    st.download_button(
                        label="📥 Download Itinerary as Text",
                        data=itinerary,
                        file_name=f"tripmate_{destination.lower().replace(' ','_')}_itinerary.txt",
                        mime="text/plain"
                    )

            except Exception as e:
                st.error(f"❌ Error generating itinerary: {str(e)}\n\nPlease check your API key in the .env file.")

# ─── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div class="footer">
  Made with ❤️ for Indian Students | TripMate AI Travel Planner<br>
  Inspired by GT Holidays, Zostel & Backpacker India
</div>
""", unsafe_allow_html=True)