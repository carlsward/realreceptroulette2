import random
from typing import List

import pandas as pd
import streamlit as st


# ---------- Datainläsning ----------

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    """
    Läser in Livsmedelsverkets livsmedelsdatabas.

    Antaganden (anpassa vid behov):
    - De två första raderna är rubriker/beskrivning.
    - Rad 3 innehåller kolumnnamn.
    - Kolumnen med livsmedelsnamn heter 'Livsmedelsnamn'.
    """
    # Om din fil inte är .xlsx kan du byta till t.ex. pd.read_csv
    df = pd.read_excel(
        path,
        header=2,        # 0-baserad indexering: rad 3 är header
        engine="openpyxl"
    )

    # Filtrera bort rader utan livsmedelsnamn
    df = df[df["Livsmedelsnamn"].notna()].copy()

    # Plocka bara med kolumner vi ev. behöver senare
    return df[["Livsmedelsnamn"]]


# ---------- Generering av recept ----------

def slumpa_ingredienser(df: pd.DataFrame, antal: int) -> List[str]:
    antal = min(antal, len(df))
    ingredienser = (
        df["Livsmedelsnamn"]
        .dropna()
        .sample(antal, replace=False)
        .tolist()
    )
    return ingredienser


def generera_recept_namn(ingredienser: List[str]) -> str:
    bas_namn = [
         "Kaotisk gryta",
    "Improviserad torsdagsmiddag",
    "Kylskåpsroulette",
    "Freestylad festmåltid",
    "Kulinarisk chansning",
    "Experimentell husmansklassiker",
    "Anarkistisk enpanna",
    "Nödlösningssoppa",
    "Spontan stekpannefest",
    "Våghalsig vardagsröra",
    "Kreativ katastrofgryta",
    "Överraskningslåda från skafferiet",
    "Total smakroulette",
    "Matlådelotto",
    "Oplanerad söndagsmiddag",
    "Kaos i kastrullen",
    "Improviserad lyxgryta",
    "Sista-minuten-middag",
    "Restfest Royale",
    "Fullständig smakexplosion",
    "Högoddsarmiddag",
    "Skapelse från ingenstans",
    "Halvseriös helggryta",
    "Matlagning på känn",
    "Vild chansningsgryta",
    "Kreativ kylskåpsrensning",
    "Absurd aftonmiddag",
    "Kokkonst utan manual",
    "Inre-kockens-uppror",
    "Kaotisk bjudrätt",
    "Improviserad mästerkocksdröm",
    "Det stora smakexperimentet",
    "Husmorsknep på steroider",
    "Logiklöst långkok",
    "Osorterad smakbuffé",
    "Friformsgryta",
    "Receptlös festanrättning",
    "Magkänsle-middag",
    "Kulinariskt lyckokast",
    "Total improvisationsbuffé",
    ]
    stilar = [
        "à la Recept Roulette",
    "med oväntad twist",
    "som ingen bad om",
    "för modiga gäster",
    "deluxe",
    "med fullständig smakrisk",
    "enligt principen 'det löser sig'",
    "för den äventyrlige hemmakocken",
    "med tveksam elegans",
    "med tveksamt självförtroende",
    "inspirerad av kylskåpets innehåll",
    "utan säkerhetsbälte",
    "direkt ur fantasin",
    "med maximal improvisation",
    "som utmanar alla matkoder",
    "som förvirrar men imponerar",
    "för dig som gillar överraskningar",
    "utan några som helst garantier",
    "för modiga smaklökar",
    "med oväntade kombinationer",
    "som chockar både värd och gäst",
    "i komplett kaosutförande",
    "som får grannarna att undra",
    "i semi-professionell tappning",
    "som borde ha testats på mindre publik",
    "med hög experimentfaktor",
    "för avancerad spontankockning",
    "med tveksam vetenskaplig grund",
    "som smakar bättre än den låter",
    "som låter värre än den smakar",
    "för dig som litar på ödet",
    "i kreativ panikstil",
    "som uppfanns i sista stund",
    "för den tidsoptimistiske kocken",
    "med fullständig receptfrihet",
    "som kan bli en klassiker eller katastrof",
    "för dig som gillar mat med historia, men utan recept",
    "som i teorin borde fungera",
    "som bevis på ren matgalenskap"
    ]
    return f"{random.choice(bas_namn)} {random.choice(stilar)}"


def generera_instruktioner(ingredienser: List[str]) -> str:
    steg_templates = [
        "Stek **{ing}** i {tid} minuter på medelvärme tills det ser någorlunda ätbart ut.",
        "Koka **{ing}** försiktigt i {tid} minuter. Sluta när du börjar bli orolig.",
        "Riv **{ing}** till fina strimlor och låtsas att det var planerat från början.",
        "Tärna **{ing}** i slumpmässiga storlekar och kalla det 'rustikt'.",
        "Bryn **{ing}** snabbt och häv sedan allt i en kastrull som om du vet vad du gör.",
        "Blanda **{ing}** med allt annat och säg högt att detta är 'hemligt familjerecept'.",
        "Grilla **{ing}** tills den ser socialt acceptabel ut på bild.",
        "Finputsa **{ing}** och arrangera på tallriken som om du ska få en stjärna i någon guide.",
    ]

    steg_text = []
    for i, ing in enumerate(ingredienser, start=1):
        template = random.choice(steg_templates)
        tid = random.randint(3, 12)
        text = template.format(ing=ing, tid=tid)
        steg_text.append(f"{i}. {text}")

    avslut = [
        "Avsluta med att smaka av. Om det är gott: häv ur dig att det var busenkelt. "
        "Om det inte är gott: kalla det 'konceptuellt'.",
        "Servera direkt. Låtsas att just denna kombination är trendig i någon storstad.",
        "Toppa allt med valfri livskris och servera med ett självsäkert leende.",
    ]
    steg_text.append(f"{len(ingredienser) + 1}. {random.choice(avslut)}")

    return "\n".join(steg_text)


def generera_portioner() -> int:
    return random.choice([1, 2, 3, 4])


# ---------- Streamlit-app ----------

def main():
    st.set_page_config(
        page_title="Recept Roulette",
        layout="centered"
    )

    # ---------- GLOBAL STYLING & ANIMATION ----------
    st.markdown(
        """
        <style>
        :root {
            --bg-gradient: radial-gradient(circle at top left, #f9fafb 0, #e5e7eb 40%, #d1d5db 100%);
            --card-bg: #ffffff;
            --border-subtle: #e5e7eb;
            --accent: #111827;
            --accent-soft: #4b5563;
        }

        .stApp {
            background: var(--bg-gradient);
        }

        .main {
            max-width: 900px;
            margin: 0 auto;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* Titel / header */
        .rr-header {
            text-align: center;
            margin-bottom: 2.5rem;
            animation: fadeInDown 0.6s ease-out;
        }
        .rr-title {
            font-size: 2.4rem;
            font-weight: 650;
            letter-spacing: -0.03em;
            color: var(--accent);
        }
        .rr-subtitle {
            margin-top: 0.4rem;
            font-size: 0.98rem;
            color: var(--accent-soft);
        }

        /* Receptkort */
        .recept-kort {
            background: var(--card-bg);
            padding: 1.9rem 1.8rem;
            border-radius: 1.4rem;
            border: 1px solid var(--border-subtle);
            box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
            backdrop-filter: blur(6px);
            animation: floatIn 0.55s ease-out;
        }

        .sektion-rubrik {
            font-weight: 600;
            margin-top: 1.4rem;
            margin-bottom: 0.4rem;
            font-size: 1rem;
            color: var(--accent);
        }

        /* Knapp-styling */
        .stButton>button {
            border-radius: 999px;
            padding: 0.6rem 1.7rem;
            border: 1px solid #111827;
            background: #111827;
            color: #f9fafb;
            font-weight: 500;
            letter-spacing: 0.03em;
            text-transform: uppercase;
            font-size: 0.78rem;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.35);
            transition:
                transform 0.12s ease-out,
                box-shadow 0.12s ease-out,
                background 0.15s ease-out,
                border-color 0.15s ease-out;
        }

        .stButton>button:hover {
            transform: translateY(-1px) scale(1.01);
            box-shadow: 0 16px 40px rgba(15, 23, 42, 0.45);
            background: #020617;
            border-color: #020617;
        }

        .stButton>button:active {
            transform: translateY(0) scale(0.99);
            box-shadow: 0 6px 20px rgba(15, 23, 42, 0.28);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: #111827;
        }
        section[data-testid="stSidebar"] * {
            color: #e5e7eb !important;
        }
        section[data-testid="stSidebar"] .stSlider label,
        section[data-testid="stSidebar"] label {
            font-size: 0.85rem !important;
        }

        /* Enkla keyframe-animationer */
        @keyframes floatIn {
            0% {
                opacity: 0;
                transform: translateY(14px) scale(0.98);
            }
            100% {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        @keyframes fadeInDown {
            0% {
                opacity: 0;
                transform: translateY(-12px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ---------- SIDEBAR ----------
    with st.sidebar:
        st.header("Inställningar")
        antal_ingredienser = st.slider("Antal ingredienser", min_value=2, max_value=7, value=4)
        filnamn = st.text_input(
            "Filnamn på livsmedelsdatabasen",
            value="LivsmedelsDB_202511142228.xlsx",
            help="Filen ska ligga i samma mapp som denna app.",
        )
        st.caption("Justera namnet här om din fil heter något annat.")

    # ---------- HEADER ----------
    st.markdown(
        """
        <div class="rr-header">
            <div class="rr-title">Recept Roulette</div>
            <div class="rr-subtitle">
                Slumpa fram oväntade kombinationer från Livsmedelsverkets databas
                och få ett humoristiskt receptförslag.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not filnamn:
        st.error("Ange ett filnamn för databasen i sidomenyn.")
        return

    # ---------- DATA ----------
    try:
        df = load_data(filnamn)
    except FileNotFoundError:
        st.error(f"Filen '{filnamn}' hittades inte. Kontrollera att den ligger i samma mapp som appen.")
        return
    except Exception as e:
        st.error(f"Ett fel uppstod vid inläsning av filen: {e}")
        return

    if len(df) == 0:
        st.error("Databasen innehåller inga livsmedel efter filtrering. Kontrollera kolumnnamn och header-rad.")
        return

    # ---------- HUVUDFUNKTION ----------
    knapp = st.button("Generera recept")

    if knapp:
        ingredienser = slumpa_ingredienser(df, antal_ingredienser)
        recept_namn = generera_recept_namn(ingredienser)
        portioner = generera_portioner()
        instruktioner = generera_instruktioner(ingredienser)

        st.markdown("<div class='recept-kort'>", unsafe_allow_html=True)
        st.markdown(f"### {recept_namn}")
        st.markdown(f"*Ca {portioner} portion(er)*")

        st.markdown("<div class='sektion-rubrik'>Ingredienser</div>", unsafe_allow_html=True)
        ingrediens_lista = "\n".join([f"- {ing}" for ing in ingredienser])
        st.markdown(ingrediens_lista)

        st.markdown("<div class='sektion-rubrik'>Gör så här</div>", unsafe_allow_html=True)
        st.markdown(instruktioner)

        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Tryck på knappen för att slumpa fram ett nytt recept.")



if __name__ == "__main__":
    main()
