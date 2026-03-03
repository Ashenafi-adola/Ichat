import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import  NavBar  from './components/navbar'
import Home from './pages/home'
import LogInPage from './pages/auth'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <NavBar/> 
      <Home/> 
      <LogInPage/>
    </>
  )
}

export default App
