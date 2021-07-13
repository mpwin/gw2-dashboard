import React from 'react';
import axios from 'axios';
import classNames from 'classnames';

class Collection extends React.Component {
  constructor(props) {
    super(props);
    this.state = { skins: [] };
    this.order = {
      'Sword':      1,  'Hammer': 2, 'Longbow': 3,  'Shortbow': 4,  'Axe':     5,  'Dagger':   6,
      'Greatsword': 7,  'Mace':   8, 'Pistol':  9,  'Rifle':    10, 'Scepter': 11, 'Staff':    12,
      'Focus':      13, 'Torch': 14, 'Warhorn': 15, 'Shield':   16, 'Spear':   17, 'Speargun': 18,
      'Trident':    19,

      'Helm': 1, 'Shoulders': 2, 'Coat': 3, 'Gloves': 4, 'Leggings': 5, 'Boots': 6
    };
  }

  componentDidUpdate(prevProps) {
    if (this.props.collection != prevProps.collection) {
      axios.get(`/api/collections/${this.props.collection.id}.json`)
        .then(res => {
          let skins = res.data.skins.sort((a, b) => {
            return (this.order[a.bracket] - this.order[b.bracket]);
          });

          this.setState({ skins: skins });
        });
    }
  }

  render() {
    if (this.props.collection) {
      var skins = this.state.skins.map((skin) => {
        return(
          <li className={classNames({ 'unlocked': skin.unlocked })}>
            {skin.name}
          </li>
        );
      });

      return(
        <ul>
          <li className='active'>{this.props.collection.name}</li>
          {skins}
        </ul>
      );
    }
    else {
      return(<ul></ul>);
    }
  }
}

export default Collection;
