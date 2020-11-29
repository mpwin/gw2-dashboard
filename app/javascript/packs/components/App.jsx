import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import Dashboard from './Dashboard';

document.addEventListener('DOMContentLoaded', () => {
  ReactDOM.render(
    <Router>
      <Route path='/' component={Dashboard} />
    </Router>,
    document.getElementById('dashboard'),
  )
});
