import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/contacts")
      .then((res) => res.json())
      .then((data) => setContacts(data))
      .catch((err) => console.error("Erreur de chargement:", err));
  }, []);

  return (
    <div className="App">
      <h1>Carnet de Contacts</h1>
      <ul>
        {contacts.map((contact) => (
          <li key={contact.id}>
            <strong>{contact.name}</strong> - {contact.email} - {contact.phone}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
