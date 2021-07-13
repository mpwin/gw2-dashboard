import React from 'react'
import classNames from 'classnames'

class SkinList extends React.Component {
  render() {
    var skins = this.props.skins.map((skin) => {
      return (
        <li className={classNames({ 'unlocked': skin.unlocked })}>
          {skin.name}
        </li>
      )
    })

    return(
      <ul>
        <li className='active'>{this.props.name}</li>
        {skins}
      </ul>
    )
  }
}

export default SkinList;
