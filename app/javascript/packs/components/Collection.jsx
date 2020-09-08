import React from 'react';
import axios from 'axios';
import classNames from 'classnames';

class Collection extends React.Component {
  constructor(props) {
    super(props);
    this.state = { skins: [] };
    this.order = { 'Helm': 1, 'Shoulders': 2, 'Coat': 3, 'Gloves': 4, 'Leggings': 5, 'Boots': 6 };
  }

  componentDidUpdate(prevProps) {
    if (this.props.collection != prevProps.collection) {
      axios.get(`/collections/${this.props.collection.id}.json`)
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
          <li class={classNames('list-group-item', { 'list-group-item-success': skin.unlocked })}>
            {skin.name}
          </li>
        );
      });

      return(
        <ul class='list-group text-monospace'>
          <li class='list-group-item active'>{this.props.collection.name}</li>
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
