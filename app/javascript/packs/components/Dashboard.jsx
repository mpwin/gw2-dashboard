import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'
import Collection from './Collection'
import Collections from './Collections'

class Dashboard extends React.Component {
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

  showCollection = (collection) => {
    this.setState({ collection: collection.name });
  }

  groupBy = (key, array) =>
    array.reduce((objectsByKeyValue, obj) => {
      const value = obj[key];
      objectsByKeyValue[value] = (objectsByKeyValue[value] || []).concat(obj);
      return objectsByKeyValue;
    }, {});
  
  componentDidMount() {
    axios.get('/collections.json')
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
      <div class='container-fluid mt-4'>
        <div class='row'>
          <div class='col-2'><Collection collection={this.state.collection} /></div>
          <div class='col-2'></div>
          <div class='col-2'><Collections name='Weapon'       collections={this.state.weapon}       showCollection={this.showCollection} /></div>
          <div class='col-2'><Collections name='Heavy Armor'  collections={this.state.heavy_armor}  showCollection={this.showCollection} /></div>
          <div class='col-2'><Collections name='Medium Armor' collections={this.state.medium_armor} showCollection={this.showCollection} /></div>
          <div class='col-2'><Collections name='Light Armor'  collections={this.state.light_armor}  showCollection={this.showCollection} /></div>
        </div>
      </div>
    );
  }
}

document.addEventListener('turbolinks:load', () => {
  const app = document.getElementById('dashboard')
  app && ReactDOM.render(<Dashboard />, app)
})
