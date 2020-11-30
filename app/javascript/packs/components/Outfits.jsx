import React from 'react';
import classNames from 'classnames';

class Outfits extends React.Component {
  constructor(props) {
    super(props);
    this.state = { outfits: [] };
  }

  componentDidMount() {
    fetch('/api/outfits.json')
      .then((response) => { return response.json() })
      .then((data)     => { this.setState({ outfits: data }) });
  }

  render() {
    var outfits = this.state.outfits.map((outfit) => {
      return (
        <li className={classNames('list-group-item', { 'list-group-item-success': outfit.unlocked })}>
          {outfit.name}
        </li>
      );
    });

    return (
      <div className='container-fluid mt-4'>
        <div className='row'>
          <div className='col-2'>
            <ul className='list-group text-monospace'>
              <li className='list-group-item active'>Outfits</li>
              {outfits}
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default Outfits;
