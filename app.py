# import streamlit as st
# from managerNota import ManagerNota
#
# # # Path to the file where notes will be saved
# # FILE_PATH = "notes.json"
# #
# # # Initialize note manager
# # manager = ManagerNota(FILE_PATH)
#
# # Inițializăm managerul de note
# manager = ManagerNota()
#
# st.title('Aplicație de Note')
#
# # Formular pentru adăugarea unei noi note
# with st.form("add_note"):
#     st.write("Adaugă o nouă notă")
#     titlu = st.text_input("Titlu")
#     continut = st.text_area("Conținut")
#     submit_button = st.form_submit_button("Adaugă Nota")
#
#     if submit_button:
#         manager.adauga_nota(titlu, continut)
#         st.success("Nota adăugată cu succes!")
#
# # Afișează note existente
# st.write("Notele tale")
# for index, nota in enumerate(manager.notes):
#     with st.expander(f"{nota.titlu} - {nota.data_crearii.strftime('%Y-%m-%d %H:%M:%S')}"):
#         st.write(f"Conținut: {nota.continut}")
#         st.write(f"Status: {nota.status}")
#
#         # Buton pentru a șterge nota
#         if st.button(f"Șterge", key=f"delete_{index}"):
#             manager.sterge_nota(index)
#             st.experimental_rerun()
#
# # Căutarea notelor
# st.write("Caută în note")
# search_query = st.text_input("Cuvânt cheie")
# if st.button("Caută"):
#     rezultate = manager.cauta_nota(search_query)
#     if rezultate:
#         for nota in rezultate:
#             st.write(f"{nota.titlu} - {nota.data_crearii.strftime('%Y-%m-%d %H:%M:%S')}")
#             st.write(f"Conținut: {nota.continut}")
#             st.write(f"Status: {nota.status}")
#     else:
#         st.write("Nicio notă găsită.")
#

##########################################
# app.py

import streamlit as st
from managerNota import ManagerNota

# Inițializăm managerul de note
manager = ManagerNota()

st.title('Aplicație de Note')

# Formular pentru adăugarea unei noi note
with st.form("add_note"):
   st.write("Adaugă o notiță nouă")
   titlu = st.text_input("Titlu")
   continut = st.text_area("Conținut")
   submit_button = st.form_submit_button("Adaugă notiță")

   if submit_button:
       st.session_state.clicked_buttons.append("Create_new_note")
       manager.adauga_nota(titlu, continut)
       st.success("Nota adăugată cu succes!")

col_todo, col_in_progress, col_done, col_canceled = st.columns(4)

if 'clicked_buttons' not in st.session_state:
   st.session_state.clicked_buttons = []

with col_todo:
   # st.header("To Do")
   st.markdown("<h3 style='text-align: left; color: #1f77b4; font-size: 20px; '>To Do</h3>", unsafe_allow_html=True)
   for nota in [n for n in manager.note if n.status == "în curs"]:
       with st.expander(f"{nota.titlu}"):
           st.write(f"Conținut: {nota.continut}")
           key = "progress_" + str(nota.id)[-12:]
           if st.button("Muta în In Progress", key=key):
               st.session_state.clicked_buttons.append(key)
               manager.schimba_status_nota(nota.id, "în progres")
           key = "cancel_" + str(nota.id)[-12:]
           if st.button("Muta în Canceled", key=key):
               st.session_state.clicked_buttons.append(key)
               manager.schimba_status_nota(nota.id, "Canceled")
               st.rerun()

with col_in_progress:
   # st.header("In Progress")
   st.markdown("<h3 style='text-align: left; color: #1f77b4; font-size: 20px; '>In Progress</h3>", unsafe_allow_html=True)
   for nota in [n for n in manager.note if n.status == "în progres"]:
       with st.expander(f"{nota.titlu}"):
           st.write(f"Conținut: {nota.continut}")
           key = "done_" + nota.id[-12:]
           if st.button("Muta în Done", key=key):
               st.session_state.clicked_buttons.append(key)
               manager.schimba_status_nota(nota.id, "finalizat")
               st.rerun()

with col_done:
   # st.header("Done")
   st.markdown("<h3 style='text-align: left; color: #1f77b4; font-size: 20px; '>Done</h3>", unsafe_allow_html=True)
   for nota in [n for n in manager.note if n.status == "finalizat"]:
       with st.expander(f"{nota.titlu}"):
           st.write(f"Conținut: {nota.continut}")
           key = "delete_" + nota.id[-12:]
           if st.button("Șterge", key=key):
               st.session_state.clicked_buttons.append(key)
               manager.sterge_nota(nota.id)
               st.rerun()

with col_canceled:
   # st.header("Canceled")
   st.markdown("<h3 style='text-align: left; color: #800080; font-size: 20px; '>Canceled</h3>", unsafe_allow_html=True)
   for nota in [n for n in manager.note if n.status == "Canceled"]:
       with st.expander(f"{nota.titlu}"):
           st.write(f"Conținut: {nota.continut}")
           key = "delete_" + str(nota.id)[-12:]
           if st.button("Șterge", key=key):
               st.session_state.clicked_buttons.append(key)
               manager.sterge_nota(nota.id)
               st.rerun()

# # Display the IDs of clicked buttons
# st.write("Clicked button IDs:", st.session_state.clicked_buttons)

# # Căutarea notelor
# # st.write("Caută în note")
# st.markdown("<h3 style='text-align: left; color: #FFFFFF; font-size: 20px; '>Caută în note</h3>", unsafe_allow_html=True)
# search_query = st.text_input("Cuvânt cheie")
# if st.button("Caută"):
#     rezultate = manager.cauta_nota(search_query)
#     if rezultate:
#         for nota in rezultate:
#             st.write(f"{nota.titlu} - {nota.data_crearii.strftime('%Y-%m-%d %H:%M:%S')}")
#             st.write(f"Conținut: {nota.continut}")
#             st.write(f"Status: {nota.status}")
#     else:
#         st.write("Nicio notă găsită.")

# # Butonul pentru editare
#     edit_button_key = "edit_" + str(nota.id)[-12:]  # Generăm un ID unic pentru butonul de editare
#     if st.button("Editare", key=edit_button_key):
#         st.session_state.clicked_buttons.append(edit_button_key)
#          # Acțiunile pentru editarea notei, de exemplu deschiderea unei pagini de editare sau afișarea unui formular de editare


######
# Inițializăm managerul de note
manager = ManagerNota()

st.title('Listare, Căutare și Editare Note')

# Câmp de căutare pentru filtrarea notelor după nume
cuvant_cheie = st.text_input('Caută note după nume:', '')

# Filtrăm notele în funcție de cuvântul cheie introdus
note_filtrate = manager.cauta_nota(cuvant_cheie) if cuvant_cheie else manager.note

# Afișăm notele filtrate
for nota in note_filtrate:
   with st.expander(f"{nota.titlu}"):
       # Afisează detalii despre notă
       # st.write(f"Conținut: {nota.continut}")

       # Formular pentru editarea notei
       with st.form(f"form_edit_{nota.id}"):
           new_titlu = st.text_input("Titlu", value=nota.titlu, key=f"titlu_{nota.id}")
           new_continut = st.text_area("Conținut", value=nota.continut, key=f"continut_{nota.id}")
           submit_edit = st.form_submit_button("Salvează Modificările")

           if submit_edit:
               # Apelăm o metodă care să actualizeze nota bazată pe ID
               manager.modifica_nota(nota.id, new_titlu, new_continut)
               st.success("Nota a fost actualizată cu succes!")
               # Reîncarcă pagina pentru a reflecta modificările
               st.rerun()