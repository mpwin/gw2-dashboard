import React from 'react';
import axios from 'axios';
import classNames from 'classnames';

class Collection extends React.Component {
  constructor(props) {
    super(props);
    this.state = { skins: [] };
  }

  componentDidUpdate(prevProps) {
    if (this.props.collection != prevProps.collection) {
      axios.get(`/collections/${this.props.collection.id}.json`)
        .then(res => {
          this.setState({ skins: res.data.skins });
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
