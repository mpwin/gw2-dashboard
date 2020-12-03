import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Dyes from './Dyes';
import Outfits from './Outfits';
import Wardrobe from './Wardrobe';

document.addEventListener('DOMContentLoaded', () => {
  ReactDOM.render(
    <Router>
      <Switch>
        <Route path='/' exact  component={Wardrobe} />
        <Route path='/dyes'    component={Dyes} />
        <Route path='/outfits' component={Outfits} />
      </Switch>
    </Router>,
    document.getElementById('dashboard'),
  )
});
