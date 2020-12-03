import React from 'react';
import axios from 'axios';

import Collection from './Collection';
import CollectionList from './CollectionList';
import Skins from './Skins';

class Wardrobe extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      collection:   null,
      weapon:       [],
      heavy_armor:  [],
      medium_armor: [],
      light_armor:  []
    };
  }

  selectCollection = (collection) => {
    this.setState({ collection: collection });
  }

  groupBy = (key, array) =>
    array.reduce((objectsByKeyValue, obj) => {
      const value = obj[key];
      objectsByKeyValue[value] = (objectsByKeyValue[value] || []).concat(obj);
      return objectsByKeyValue;
    }, {});
  
  componentDidMount() {
    axios.get('/api/collections.json')
      .then(res => {
        const collections = this.groupBy('category', res.data);
        const armor       = this.groupBy('weight_class', collections.Armor);

        this.setState({
          weapon:       collections.Weapon || [],
          heavy_armor:  armor.Heavy        || [],
          medium_armor: armor.Medium       || [],
          light_armor:  armor.Light        || []
        });
      });
  }

  render() {
    return (
      <div className='container-fluid mt-4'>
        <div className='row'>
          <div className='col-2'><Collection collection={this.state.collection} /></div>
          <div className='col-2'><CollectionList name='Weapon'       collections={this.state.weapon}       selectCollection={this.selectCollection} selectedCollection={this.state.collection} /></div>
          <div className='col-2'><CollectionList name='Heavy Armor'  collections={this.state.heavy_armor}  selectCollection={this.selectCollection} selectedCollection={this.state.collection} /></div>
          <div className='col-2'><CollectionList name='Medium Armor' collections={this.state.medium_armor} selectCollection={this.selectCollection} selectedCollection={this.state.collection} /></div>
          <div className='col-2'><CollectionList name='Light Armor'  collections={this.state.light_armor}  selectCollection={this.selectCollection} selectedCollection={this.state.collection} /></div>
          <div className='col-2'><Skins /></div>
        </div>
      </div>
    );
  }
}

export default Wardrobe;
