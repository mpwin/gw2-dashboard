import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <div className='container-fluid mt-4'>
      <div className='row'>
        <div className='col-md-8 offset-md-2'>
          <nav className='navbar navbar-expand-lg'>
            <ul className='navbar-nav'>
              <li className='nav-item'><Link to='/' className='nav-link'>Wardrobe</Link></li>
              <li className='nav-item'><Link to='/dyes' className='nav-link'>Dyes</Link></li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  );
}

export default Navbar;
