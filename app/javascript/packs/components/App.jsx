import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Dashboard from './Dashboard';
import Outfits from './Outfits';

document.addEventListener('DOMContentLoaded', () => {
  ReactDOM.render(
    <Router>
      <Switch>
        <Route path='/' exact component={Dashboard} />
        <Route path='/outfits' component={Outfits} />
      </Switch>
    </Router>,
    document.getElementById('dashboard'),
  )
});
