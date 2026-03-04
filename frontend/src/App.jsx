import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import  NavBar  from './components/navbar'
import Home from './pages/home'
import LogInPage from './pages/auth'
import ChatArea from './components/ChatArea'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <NavBar/> 
      <Home/> 
      <ChatArea/>
    </>
  )
}

export default App
