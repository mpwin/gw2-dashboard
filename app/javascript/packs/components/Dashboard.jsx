import React from 'react'
import ReactDOM from 'react-dom'
import Collections from './Collections'

class Dashboard extends React.Component {
  render() {
    return (
      <div class='container-fluid'>
        <h1>Dashboard</h1>
        
        <Collections />
      </div>
    );
  }
}

document.addEventListener('turbolinks:load', () => {
  const app = document.getElementById('dashboard')
  app && ReactDOM.render(<Dashboard />, app)
})
