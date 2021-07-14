import React from 'react';
import { NavLink } from 'react-router-dom';

const Navbar = () => {
  return (
    <div id='navbar'>
      <div id='nav'>
        <NavLink exact to='/'>Wardrobe</NavLink>
        <NavLink to='/dyes'>Dyes</NavLink>
      </div>
    </div>
  );
}

export default Navbar;
