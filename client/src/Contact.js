import React from 'react'

export default function Contact() {
    const [email,setEmail] = useState("")
    const [body, setBody] = useState("")
    const setEmail = (e) =>{
        e.preventdefault()
        
    }
    return (
        <div>
            <input value = {email} onChange = {e => setEmail(e.target.value)} placeholder = "email here"></input>
            <input value = {body} onChange = {e => setBody(e.target.value)} placeholder = "email here"></input>
            <button onSubmit = {sendEmail}/>
        </div>
    )
}
