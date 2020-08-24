require 'rails_helper'

RSpec.describe Skin, type: :model do
  it { should serialize(:flags) }
  it { should serialize(:restrictions) }

  describe 'associations' do
    it { should belong_to(:collection).optional }

    it 'updates its collection when its unlocked field is changed' do
      skin = Skin.create(unlocked: false)
      skin.create_collection
      expect(skin.collection.unlocked).to eq(false)

      skin.update(unlocked: true)
      expect(skin.collection.unlocked).to eq(true)
    end
  end
end
