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
        <li className={classNames({ 'unlocked': outfit.unlocked })}>
          {outfit.name}
        </li>
      );
    });

    return (
      <div className='container'>
        <ul>
          <li className='active'>Outfits</li>
          {outfits}
        </ul>
      </div>
    );
  }
}

export default Outfits;
