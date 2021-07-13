import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <ul>
      <li><Link to='/'>Wardrobe</Link></li>
      <li><Link to='/dyes'>Dyes</Link></li>
    </ul>
  );
}

export default Navbar;
