import React from 'react';
import classNames from 'classnames';

class Dyes extends React.Component {
  constructor(props) {
    super(props);
    this.state = { dyes: [] };
  }

  componentDidMount() {
    fetch('/api/dyes.json')
      .then((response) => { return response.json() })
      .then((data)     => { this.setState({ dyes: data }) });
  }

  render() {
    var dyes = this.state.dyes.map((dye) => {
      return (
        <li className={classNames({ 'unlocked': dye.unlocked })}>
          {dye.name}
        </li>
      );
    });

    return (
      <div className='container'>
        <ul>
          <li className='active'>Dyes</li>
          {dyes}
        </ul>
      </div>
    );
  }
}

export default Dyes;
