import React from 'react'
import classNames from 'classnames'

class Skins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      skins: []
    };
  }

  componentDidMount() {
    fetch('/skins.json')
      .then((response) => { return response.json() })
      .then((data)     => { this.setState({ skins: data }) });
  }

  render() {
    var skins = this.state.skins.map((skin) => {
      return (
        <li class={classNames('list-group-item', { 'list-group-item-success': skin.unlocked })}>
          {skin.name}
        </li>
      )
    })

    return(
      <ul class='list-group text-monospace'>
        {skins}
      </ul>
    )
  }
}

export default Skins;
