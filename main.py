"""This is a Streamlit app for collecting event invitation responses."""

import streamlit as st
import re
from src.modules import session, User

# Set the page configuration
st.set_page_config(layout="wide")

if "finalizat" not in st.session_state:
    st.session_state.finalizat = False

def finalizeaza_raspuns():
    """
    Callback function to finalize the user's response.

    Sets the session state 'finalizat' to True.
    """
    st.session_state.finalizat = True

# Add an image to the sidebar
with st.sidebar:
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Bun venit!</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image("assets/sidebar_img.png", use_container_width=True)

# Main container with two columns
col1, col2 , col3 = st.columns([1, 2, 3])

# Add content to the columns
with col1:
    st.markdown(
        """
        <div style="text-align: center;">
            <p style="font-weight:bold; font-size: 20px;">Aceasta este pagina de invitatie</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.image("assets/weed_invitation.jpg")

with col2:
    tab1, tab2, tab3, tab4 = st.tabs(["General", "Program", "Meniu", "Transport"])

    with tab1:
        st.header("Detalii Generale")
        st.text("Data și ora: Sâmbătă, 15 iunie 2025, la ora 17:00.")
        st.text("Locația ceremoniei religioase: Biserica Sf. Gheorghe, Str. Mihai Eminescu nr. 12.")
        css = """
        <style>
            .responsive-map {
                width: 400px;
                height: 250px;
                border: 0;
            }
            @media (max-width: 1596px) {
                .responsive-map {
                    width: 350px;
                    height: 250px;
                }
            }
            @media (max-width: 1450px) {
                .responsive-map {
                display:none;
                }
            }
            @media (max-width: 639px) {
                .responsive-map {
                    display: block;
                    width: 450px;
                    height: 250px;
                }
            }
            @media (max-width: 472px) {
                .responsive-map {
                    width: 250px;
                    height: 250px;
                }
            }
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
        google_maps_iframe = """
                    <iframe 
                        class="responsive-map"
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.835434509366!2d144.96305771531615!3d-37.81627944201371!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad642af0f11fd81%3A0xf577f9c6a6e51b36!2sFederation%20Square!5e0!3m2!1sen!2sau!4v1635587715237!5m2!1sen!2sau"  
                        allowfullscreen="" 
                        loading="lazy">
                    </iframe>
                    """
        st.markdown(google_maps_iframe, unsafe_allow_html=True)
        st.text("Locația petrecerii: Restaurantul Bellagio, Str. Primăverii nr. 45.")
        google_maps_iframe = """
                            <iframe 
                                class="responsive-map"
                                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.835434509366!2d144.96305771531615!3d-37.81627944201371!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad642af0f11fd81%3A0xf577f9c6a6e51b36!2sFederation%20Square!5e0!3m2!1sen!2sau!4v1635587715237!5m2!1sen!2sau"  
                                allowfullscreen="" 
                                loading="lazy">
                            </iframe>
                            """
        st.markdown(google_maps_iframe, unsafe_allow_html=True)
        st.text("Dress code: Formal (rochii elegante, costume și cravate).")

    with tab2:
        st.header("Programul Evenimentului")
        st.text("16:30 – Sosirea invitaților la biserică.")
        st.text("17:00 – Ceremonia religioasă.")
        st.text("18:30 – Sosirea la restaurant și welcome drink.")
        st.text("19:30 – Primul dans al mirilor.")
        st.text("20:00 – Servirea meniului.")
        st.text("21:00 – Distracție pe ringul de dans!")
        st.text("23:00 – Candy bar & desert special.")
        st.text("02:00 – Tăierea tortului.")

    with tab3:
        st.header("Meniul")
        st.text("Aperitiv rece: Bruschete cu somon, mix de brânzeturi, prosciutto cu pepene galben.")
        st.text("Fel principal: File de vită cu sos de ciuperci și piure de trufe, pește la cuptor cu legume.")
        st.text("Desert: Tiramisu de casă și tortul mirilor.")
        st.text("Opțiuni vegetariene: Meniu special disponibil la cerere.")
        st.text("Băuturi: Vinuri selecționate, cocktailuri, bere, suc și apă.")

    with tab4:
        st.header("Transport")
        st.text("Parcare: Parcare gratuită disponibilă la restaurant.")
        st.text("Transport: Autobuze vor fi puse la dispoziție pentru cei care nu au mașini, cu plecare din fața bisericii la ora 18:00.")
        st.text("Cazare: Pentru invitații din afara orașului, recomandăm Hotelul Royal Palace, situat la 5 minute de restaurant. Oferim discount special pentru cei care rezervă până pe 1 iunie.")

with col3:
    st.title("Detalii despre Invitați")
    st.subheader("Completează detaliile tale mai jos:")

    nume = st.text_input("Nume", placeholder="Introdu numele de familie")
    if nume:
        if nume[0].isupper() and len(nume) < 20:
            st.success("Numele este valid.")
        else:
            st.error("Prima literă a numelui trebuie să fie majusculă si lungimea de maxim 20 de caractere.")

    prenume = st.text_input("Prenume", placeholder="Introdu prenumele")
    if prenume:
        prenume_prim = prenume.split(' ')[0].split('-')[0]
        if prenume_prim[0].isupper() and len(prenume) < 40:
            st.success("Prenumele  este valid.")
        else:
            st.error("Prenumele trebuie să înceapă cu literă mare, să fie despartit de spațiu sau '-'! si lungimea de maxim 40 de caractere.")

    telefon = st.text_input("Număr de telefon", placeholder="Introdu numărul de telefon")
    numar_strain = st.checkbox("Am un număr de telefon străin")
    if telefon:
        if numar_strain:
            if telefon.startswith("+") and 8 < len(telefon) < 20:
                st.success("Mulțumim! Numărul de telefon internațional este valid.")
            elif len(telefon) > 20:
                st.error("Numărul de telefon este prea lung! Te rugăm să introduci un număr valid.")
            else:
                st.error("Te rog să introduci numărul complet, începând cu '+' și codul țării!")
        else:
            if re.fullmatch(r"07\d{8}", telefon):
                st.success("Numărul de telefon este valid.")
            else:
                st.error("Numărul de telefon este invalid! Asigură-te că are 10 cifre și începe cu 07.")

    particip = st.radio("Vei participa la eveniment?", ("Particip", "Nu particip"))
    motiv_neparticipare = None  # Inițializăm variabila pentru motive
    if particip == "Nu particip":
        motiv_neparticipare = st.text_area("Te rugăm să ne spui motivul!",
                                           placeholder="Feedback-ul tau este important pentru noi deoarece ne ajută să ne îmbunătățim!")
        if motiv_neparticipare:
            st.success("Mulțumim pentru răspunsul tău!")
    else:
        st.success("Ne bucurăm că vei fi alături de noi!")

    extra_details = st.checkbox("Daca ai orice de adaugat te rog sa ne spui:")
    extra_details_text = None  # Inițializăm variabila pentru detalii suplimentare
    if extra_details:
        extra_details_text = st.text_area("Extra", placeholder="Te rugam să detaliezi cat mai explicit, ca sa te putem ajuta!")

    if st.button("Trimite"):
        with st.container():
            st.markdown("<h2 style='text-align: center;'>Rezumatul Răspunsurilor</h2>", unsafe_allow_html=True)
            st.write(f"**Nume:** {nume}")
            st.write(f"**Prenume:** {prenume}")
            st.write(f"**Număr de telefon:** {telefon} {'(Număr străin)' if numar_strain else '(Număr românesc)'}")
            st.write(f"**Participare:** {particip}")
            if particip == "Nu particip":
                st.write(
                    f"**Motiv pentru neparticipare:** {motiv_neparticipare if motiv_neparticipare else 'Niciun motiv specificat.'}")
            if extra_details:
                st.write(
                    f"**Detalii suplimentare:** {extra_details_text if extra_details_text else 'Nicio detaliere adăugată.'}")
            else:
                st.write("**Detalii suplimentare:** Nu au fost adăugate detalii suplimentare.")

            # Adăugăm butonul "Finalizează"
            if st.button("Finalizează", key="finalizeaza", on_click=finalizeaza_raspuns):
                pass

if st.session_state.finalizat:
    if not nume or not prenume or not telefon:
        st.error("Toate câmpurile obligatorii trebuie completate!")
    else:
    # Creează o sesiune SQLAlchemy
        user = User(firstname = prenume,
        lastname = nume,
        phone = telefon,
        participation = particip,
        non_participants_details = motiv_neparticipare,
        extra_details = extra_details_text if extra_details else None)
        session.add(user)
        session.commit()
        session.close()
        st.success("Participant inregistrat!")

    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
            <h1 style="color: green; text-align: center;">Mulțumim! Detaliile tale au fost înregistrate cu succes!</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
         background-color: transparent;
        text-align: right;
        font-size: 14px;
        color: #555;
    }
    </style>
    <div class="footer">
        © 2025 All Rights Reserved ~Gabriel//
    </div>
    """,
    unsafe_allow_html=True
)
