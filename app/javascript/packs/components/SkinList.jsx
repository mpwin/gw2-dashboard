import React from 'react'
import classNames from 'classnames'

class SkinList extends React.Component {
  render() {
    var skins = this.props.skins.map((skin) => {
      return (
        <li className={classNames({ 'list-group-item-success': skin.unlocked })}>
          {skin.name}
        </li>
      )
    })

    return(
      <ul>
        {skins}
      </ul>
    )
  }
}

export default SkinList;
