import React from 'react'
import classNames from 'classnames'

class Skins extends React.Component {
  render() {
    var skins = this.props.skins.map((skin) => {
      return (
        <li className={classNames('list-group-item', { 'list-group-item-success': skin.unlocked })}>
          {skin.name}
        </li>
      )
    })

    return(
      <ul className='list-group text-monospace'>
        {skins}
      </ul>
    )
  }
}

export default Skins;
