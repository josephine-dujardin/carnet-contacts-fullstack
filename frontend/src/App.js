import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [contacts, setContacts] = useState([]);
  const [newContact, setNewContact] = useState({
    name: "",
    email: "",
    phone: "",
  });
  const [editingContact, setEditingContact] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/contacts")
      .then((res) => res.json())
      .then((data) => setContacts(data))
      .catch((err) => console.error("Erreur de chargement:", err));
  }, []);

  const handleChange = (e) => {
    setNewContact({ ...newContact, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const url = editingContact
      ? `http://127.0.0.1:5000/contacts/${editingContact.id}`
      : "http://127.0.0.1:5000/contacts";

    const method = editingContact ? "PUT" : "POST";

    fetch(url, {
      method: method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newContact),
    })
      .then((res) => res.json())
      .then((data) => {
        if (editingContact) {
          setContacts(
            contacts.map((contact) =>
              contact.id === editingContact.id ? data : contact
            )
          );
          setEditingContact(null);
        } else {
          setContacts([...contacts, data]);
        }
        setNewContact({ name: "", email: "", phone: "" });
      })
      .catch((err) => console.error("Erreur d'ajout/édition:", err));
  };

  const handleEdit = (contact) => {
    setEditingContact(contact);
    setNewContact({
      name: contact.name,
      email: contact.email,
      phone: contact.phone,
    });
  };

  const handleDelete = (id) => {
    fetch(`http://127.0.0.1:5000/contacts/${id}`, { method: "DELETE" })
      .then(() => {
        setContacts(contacts.filter((contact) => contact.id !== id));
      })
      .catch((err) => console.error("Erreur de suppression:", err));
  };

  return (
    <div className="App">
      <h1>Carnet de Contacts</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Nom"
          value={newContact.name}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={newContact.email}
          onChange={handleChange}
          required
        />
        <input
          type="tel"
          name="phone"
          placeholder="Téléphone"
          value={newContact.phone}
          onChange={handleChange}
          required
        />
        <button type="submit">{editingContact ? "Modifier" : "Ajouter"}</button>
      </form>

      <ul>
        {contacts.map((contact) => (
          <li key={contact.id}>
            <strong>{contact.name}</strong> - {contact.email} - {contact.phone}
            <button onClick={() => handleEdit(contact)}>Modifier</button>
            <button onClick={() => handleDelete(contact.id)}>Supprimer</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
