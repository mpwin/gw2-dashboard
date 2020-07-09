import React from 'react'
import ReactDOM from 'react-dom'

class Dashboard extends React.Component {
  render() {
    return <h1>Dashboard</h1>
  }
}

document.addEventListener('turbolinks:load', () => {
  const app = document.getElementById('dashboard')
  app && ReactDOM.render(<Dashboard />, app)
})
