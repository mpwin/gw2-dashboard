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
        <li className={classNames('list-group-item', { 'list-group-item-success': dye.unlocked })}>
          {dye.name}
        </li>
      );
    });

    return (
      <div className='container-fluid mt-4'>
        <div className='row'>
          <div className='col-2'>
            <ul className='list-group text-monospace'>
              <li className='list-group-item active'>Dyes</li>
              {dyes}
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default Dyes;
