require 'rails_helper'

RSpec.describe Collection, type: :model do
  describe 'associations' do
    it { should have_many(:skins) }

    it 'sets :category on initial skin association' do
      subject.skins << Skin.new(category: 'Weapon')
      expect(subject.category).to eq('Weapon')
    end

    it 'sets :weight_class on initial skin association' do
      subject.skins << Skin.new(category: 'Armor', weight_class: 'Heavy')
      expect(subject.weight_class).to eq('Heavy')
    end

    it 'updates :unlocked after adding a skin' do
      subject.skins << Skin.new(unlocked: true)
      expect(subject.unlocked).to eq(true)
      subject.skins << Skin.new(unlocked: false)
      expect(subject.unlocked).to eq(false)
    end

    it 'raises an error when adding a skin of a different :category' do
      subject.category = 'Weapon'
      skin = Skin.new(category: 'Armor')
      expect { subject.skins << skin }.to raise_error('Category mismatch')
    end

    it 'raises an error when adding a skin of a different :weight_class' do
      subject.weight_class = 'Heavy'
      skin = Skin.new(category: 'Armor', weight_class: 'Light')
      expect { subject.skins << skin }.to raise_error('Weight class mismatch')
    end
  end

  describe 'validations' do
    it { should validate_presence_of(:name) }
    it { should validate_presence_of(:category) }
  end
end
